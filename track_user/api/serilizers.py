from django.contrib.auth import get_user_model

from rest_framework.serializers import CharField, ModelSerializer, ValidationError

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    password2 = CharField(label='Password Confirm')

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]

        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        email = value
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email is already Registered.')
        return value

    def validate_password2(self, value):
        data = self.get_initial()
        password1 = data.get('password')
        password2 = value
        if password1 != password2:
            raise ValidationError('password does not match.')
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()

    class Meta:
        model = User
        fields = ['username', 'password', 'token']

        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = User.objects.get(username=username)
        if user:
            if not user.check_password(password):
                raise ValidationError('Incorrect Password.')

        else:
            raise ValidationError('This username is invalid.')

        return data

# user management

this is sample project to track user login using Django

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
install python3.7 x64  && mysql-installer-community-8.0.14.0
```

run this command : 
"CREATE DATABASE test_databse CHARACTER SET utf8;"

in MYSQL Command Line Client


change 
    'USER': 'admin',
    'PASSWORD': 'eslam01028878321',

with right ones you create them in installing mysql app
in "settings.py" file in this path:'/user_management/settings.py' 
### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

in '/user_management/' folder open cmd or terminal to run coming commands

```
pip install -r requirements.txt
```
to install required python libs

then

```
python manage.py makemigrations
```

then

```
python manage.py migrate
```
then

```
python manage.py runserver
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

for simple testing open browser and type: 'http://127.0.0.1:8000/'
## Built With

* [Django](https://docs.djangoproject.com/en/2.1/) - The web framework used
* [Django REST framework](https://www.django-rest-framework.org/tutorial/quickstart/) - Django REST framework is a powerful and flexible toolkit for building Web APIs
* [Crispy-Forms](https://django-crispy-forms.readthedocs.io/en/latest/index.html) -  Django application that lets you easily build, customize and reuse forms 
* [Django User Agents](https://pypi.org/project/django-user_agents/) - A django package that allows easy identification of visitor's browser, OS and device information


## Acknowledgments

* I study and follow Vitor Freitas [Django 2.1 Authentication Tutorial](https://www.youtube.com/playlist?list=PLLxk3TkuAYnryu1lEcFaBr358IynT7l7H) in previous time.
* I study Tutorial designed by  Justin Mitchel [CodingEntrepreneurs](https://www.youtube.com/user/CodingEntrepreneurs)

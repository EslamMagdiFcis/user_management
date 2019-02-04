from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class FileUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='upload_large_file/')

    def get_absolute_url(self):
        return reverse('file-details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.file.name

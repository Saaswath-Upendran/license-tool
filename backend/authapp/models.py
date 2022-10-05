from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.username


# class FileHandle(models.Model):
#     file_upload = models.FileField()
#     key = models.CharField(max_length=16)



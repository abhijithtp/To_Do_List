from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser

'''class CustomUser(AbstractUser):
    profiles=models.ManyToManyField('profile',blank=True)

class profile(models.Model):
    name=models.CharField(max_length=20)'''

class Tasks (models.Model):
    Title=models.CharField(max_length=15)
    Desc=models.TextField(max_length=225)
    date=models.DateField(auto_now_add=True)
    users = models.ManyToManyField(User, related_name='Task')

    def __str__(self):
        return self.Desc

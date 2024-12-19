from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    is_done = models.BooleanField(default=False)  # New field

class Login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
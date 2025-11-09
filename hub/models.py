from django.db import models
from django.contrib.auth.models import User

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
    
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    date = models.DateField()
    time = models.TimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_updated_by', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_deleted_by', null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='employee_photos/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


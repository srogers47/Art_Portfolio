from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    """Setting up custom user authentication and seperating user login from admin login is recommended in docs as best practice. """
    name = models.CharField(max_length=50, default='Anonymous') #Name is optional
    email = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True) #Not None 
    USERNAME_FIELD = 'username' #Use email to signin users; username to create_superuser 
    REQUIRED_FIELDS = ['email'] #Include any fields imperative to user bussiness processess here. 
    phone = models.CharField(max_length=20, blank=True, null=True) 

    session_token = models.CharField(max_length=20, default=0) #Can make this number higher.

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 





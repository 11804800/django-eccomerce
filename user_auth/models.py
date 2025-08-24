from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class CustomUser(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=100,unique=True)
    address=models.CharField(max_length=255,blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    state=models.CharField(max_length=100,blank=True,null=True)
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    
    objects=UserManager()

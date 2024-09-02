from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Account(AbstractUser):
    
    REQUIRED_FIELDS = [] # We removed default extra email field

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = "Accounts"


    

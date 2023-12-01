from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.manager import UserManager
# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('EMPLOYEE','employee'),
        ('SUPERVISOR','supervisor'),
        ('HR','hr'),
    ]
    role = models.CharField(choices=ROLE_CHOICES,max_length=50,default='employee')
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = "email", "first_name", "last_name","password"

    def _str_(self):
        return self.username

    class Meta:
        verbose_name = "users"
        verbose_name_plural = "users"

    objects = UserManager()

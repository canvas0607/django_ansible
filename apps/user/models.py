from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class UserProfile(AbstractUser):
    """
    user info
    """
    mobile = models.CharField(default="",max_length=11,verbose_name='职员手机号',help_text='职员手机号')

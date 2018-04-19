from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    """
    user info
    """
    mobile = models.CharField(default="", max_length=11, verbose_name='职员手机号', help_text='职员手机号')


class UserGroup(models.Model):
    """
    项目组 比如运维组 捕鱼组
    """
    creator = models.ForeignKey(UserProfile, verbose_name='项目组创建者', help_text='项目组创建者',
                                related_name='user_group_creator')
    group_name = models.CharField(max_length=50, verbose_name='项目组名称', help_text='项目组名称', unique=True)
    desc = models.CharField(max_length=200, verbose_name='项目描述', help_text='项目组描述')
    members = models.ManyToManyField(UserProfile, verbose_name='项目组成员', help_text='项目组成员', blank=True,
                                     related_name='user_group_members')
    manages = models.ManyToManyField(UserProfile, verbose_name='项目管理员', help_text='项目管理员', blank=True,
                                     related_name='user_group_managers')

    class Meta:
        verbose_name = '项目组'
        verbose_name_plural = verbose_name
        app_label = 'user'

    def __str__(self):
        return self.group_name

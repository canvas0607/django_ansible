from django.db import models

from user.models import UserProfile
from server.models import ServerDetail


# Create your models here.

class UserServerCommandLine(models.Model):
    """
    用户执行一条command line 记录 日志
    """
    user = models.ForeignKey(UserProfile, verbose_name='操作用户', help_text='操作用户')
    server = models.ForeignKey(ServerDetail, verbose_name='操作服务器', help_text='操作服务器')
    command = models.CharField(max_length=150, verbose_name='用户执行的命令', help_text='用户执行的命令')
    command_res = models.TextField(verbose_name='执行命令返回数据', help_text='执行命令返回数据')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')

    class Meta:
        verbose_name = '用户在服务器上面执行命令行'
        verbose_name_plural = verbose_name

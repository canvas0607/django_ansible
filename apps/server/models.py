from django.db import models
from django.utils import timezone

# Create your models here.

class ServerDetail(models.Model):
    IS_ACTIVE = ((True,'是'),(False,'否'))

    ip = models.GenericIPAddressField(verbose_name='服务器ip地址',help_text="服务器ip地址")
    name = models.CharField(default="",max_length=30,verbose_name="服务器名称",help_text='服务器名称')
    desc = models.CharField(default="",max_length=255,verbose_name="服务器详细信息",help_text='服务器详细信息')
    ssh_name = models.CharField(max_length=50,verbose_name='ssh登录账户名',help_text='ssh登录账户名')
    ssh_password = models.CharField(max_length=50,verbose_name='ssh登录密码',help_text='ssh登录密码')
    ssh_port = models.CharField(max_length=6,verbose_name='ssh端口',help_text='ssh端口',default='22')
    add_time = models.DateTimeField(verbose_name='添加时间',default=timezone.now)
    last_scan_time = models.DateTimeField(null=True,blank=True,verbose_name='上次扫描时间',help_text='上次扫描时间')
    server_is_active = models.BooleanField(verbose_name='服务器是否存活',choices=IS_ACTIVE,help_text='服务器是否存活',default=True)
    ssh_is_active = models.BooleanField(verbose_name='ssh端口是否存活',choices=IS_ACTIVE,help_text='ssh端口是否存活',default=True)
    ssh_error_msg = models.CharField(default="",blank=True,null=True,max_length=200,verbose_name='ssh连接失败原因',help_text='ssh连接失败原因')

    class Meta:
        verbose_name = '服务器信息'
        verbose_name_plural = verbose_name
        app_label = 'server'

    def __str__(self):
        return self.ip


class ServerStatus(models.Model):
    server = models.OneToOneField(ServerDetail,verbose_name='对应服务器',help_text='对应服务器',related_name='server_status')
    memory_used = models.CharField(max_length=15,verbose_name='内存使用空间大小',help_text='内存使用空间大小')
    memory_free = models.CharField(max_length=15,verbose_name='内存空置空间大小',help_text='内存空置空间大小')
    cpu_per = models.CharField(max_length=5,verbose_name='cpu使用率',help_text='cpu使用率')
    last_update_time = models.DateTimeField(verbose_name='更新时间',help_text='更新时间',auto_now=True)

    class Meta:
        verbose_name = '服务器硬件使用状况'
        verbose_name_plural= verbose_name
        app_label = 'server'

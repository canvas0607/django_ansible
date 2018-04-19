from django.db import models
from django.utils import timezone
from user.models import UserGroup
from project.models import SubProjectsServerGroup,Projects

# Create your models here.


class ComputeHouse(models.Model):
    name = models.CharField(max_length=100, verbose_name='机房名称', help_text='机房名称')
    address = models.CharField(max_length=300, verbose_name='机房地址', help_text='机房地址')

    class Meta:
        verbose_name = '机房信息'
        verbose_name_plural = verbose_name
        app_label = 'server'

class ServerDetail(models.Model):
    IS_ACTIVE = ((True, '是'), (False, '否'))
    SERVER_KIND = (
        ('1','linux'),
        ('2','windows'),
        ('3','预留')
    )

    SERVER_STATUS = (
        ('0','回收'),
        ('1','使用中'),
        ('2','待使用')
    )
    ip = models.GenericIPAddressField(verbose_name='电信ip地址)', help_text="电信ip地址")
    name = models.CharField(default="", max_length=30, verbose_name="服务器名称", help_text='服务器名称')
    desc = models.CharField(default="", max_length=255, verbose_name="服务器详细信息", help_text='服务器详细信息')
    ssh_name = models.CharField(max_length=50, verbose_name='ssh登录账户名', help_text='ssh登录账户名')
    ssh_password = models.CharField(max_length=50, verbose_name='ssh登录密码', help_text='ssh登录密码')
    ssh_port = models.CharField(max_length=6, verbose_name='ssh端口', help_text='ssh端口', default='22')
    add_time = models.DateTimeField(verbose_name='添加时间', default=timezone.now)
    last_scan_time = models.DateTimeField(null=True, blank=True, verbose_name='上次扫描时间', help_text='上次扫描时间')
    server_is_active = models.BooleanField(verbose_name='服务器是否存活', choices=IS_ACTIVE, help_text='服务器是否存活', default=True)
    ssh_is_active = models.BooleanField(verbose_name='ssh端口是否存活', choices=IS_ACTIVE, help_text='ssh端口是否存活',
                                        default=True)
    server_group = models.ForeignKey(SubProjectsServerGroup,verbose_name='所属服务器组',help_text='所属服务器组',blank=True,null=True)
    compute_house = models.ForeignKey(ComputeHouse,verbose_name='所属机房',help_text='所属机房',blank=True)
    server_kind = models.CharField(choices=SERVER_KIND,default='1',verbose_name='服务器系统',help_text='服务器系统',max_length=2)
    server_status = models.CharField(choices=SERVER_STATUS,default='1',max_length=2,verbose_name='服务器状态',help_text='服务器状态')
    union_ip = models.GenericIPAddressField(verbose_name='联通ip',help_text='联通ip',null=True)
    internal_ip = models.GenericIPAddressField(verbose_name='内网ip',help_text='内网ip',null=True)


    class Meta:
        verbose_name = '服务器信息'
        verbose_name_plural = verbose_name
        app_label = 'server'

    def __str__(self):
        return self.ip


class ServerStatus(models.Model):
    server = models.OneToOneField(ServerDetail, verbose_name='对应服务器', help_text='对应服务器',blank=True)
    memory_used = models.CharField(max_length=15, verbose_name='内存使用空间大小', help_text='内存使用空间大小')
    memory_free = models.CharField(max_length=15, verbose_name='内存空置空间大小', help_text='内存空置空间大小')
    cpu_per = models.CharField(max_length=5, verbose_name='cpu使用率', help_text='cpu使用率')
    last_update_time = models.DateTimeField(verbose_name='更新时间', help_text='更新时间', auto_now=True)

    class Meta:
        verbose_name = '服务器硬件使用状况'
        verbose_name_plural = verbose_name
        app_label = 'server'












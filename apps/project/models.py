from django.db import models
from user.models import UserProfile


# Create your models here.


class SubProjectsKind(models.Model):
    """
    子项目类型: 如简体,繁体,s0
    """
    name = models.CharField(max_length=20, verbose_name='类型名称', help_text='类型名称')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='项目添加时间', help_text='项目添加时间')
    desc = models.CharField(max_length=500, verbose_name='类型描述', help_text='类型描述')

    class Meta:
        verbose_name = '子项目类型'
        verbose_name_plural = verbose_name
        app_label = 'project'


class Projects(models.Model):
    """
    总项目,相当于 楚乔传,琅琊榜
    """
    name = models.CharField(max_length=100, verbose_name='项目名称', help_text='项目名称')
    creator = models.ForeignKey(UserProfile, verbose_name='项目创建者', help_text='项目创建则', related_name='projects_creator')
    managers = models.ManyToManyField(UserProfile, verbose_name='项目管理者', help_text='项目管理者',
                                      related_name='projects_managers')
    desc = models.CharField(max_length=500, verbose_name='项目描述', help_text='项目描述')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='项目添加时间', help_text='项目添加时间')
    members = models.ManyToManyField(UserProfile, verbose_name='项目成员', help_text='项目成员',related_name='projects_members')

    class Meta:
        verbose_name = '总项目'
        verbose_name_plural = verbose_name
        app_label = 'project'


class SubProjects(models.Model):
    """
    子项目, 相当于 简体,繁体
    """
    project = models.ForeignKey(Projects, verbose_name='所属总项目', help_text='所属总项目')
    name = models.CharField(max_length=100, verbose_name='项目名称', help_text='项目名称')
    creator = models.ForeignKey(UserProfile, verbose_name='项目创建者', help_text='项目创建则',
                                related_name='sub_projects_creator')
    managers = models.ManyToManyField(UserProfile, verbose_name='项目管理者', help_text='项目管理者')
    desc = models.CharField(max_length=500, verbose_name='项目描述', help_text='项目描述')
    kind = models.OneToOneField(SubProjectsKind, verbose_name='子项目类型', help_text='子项目类型')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='项目添加时间', help_text='项目添加时间')

    class Meta:
        verbose_name = '子项目'
        verbose_name_plural = verbose_name
        app_label = 'project'


class SubProjectsServerGroup(models.Model):
    """
    子项目服务器组,线上服组,测试服组
    """
    sub_project = models.ForeignKey(SubProjects, verbose_name='所属子项目', help_text='所属子项目')
    name = models.CharField(max_length=100, verbose_name='项目名称', help_text='项目名称')
    members = models.ManyToManyField(UserProfile, verbose_name='项目成员', help_text='项目成员')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '子项目服务器组'
        verbose_name_plural = verbose_name
        app_label = 'project'

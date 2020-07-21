
import datetime
from django.db import models
# from users.models import UserProfile
# Create your models here.

from users.models import UserProfile


class TaskMsg(models.Model):
    # username = models.ForeignKey(UserProfile, related_name='Task',null=True, blank=True,verbose_name="登陆账号名称", on_delete="")
    username = models.ForeignKey(UserProfile, related_name='Task',null=True, blank=True,verbose_name="登陆账号名称", on_delete=models.SET_NULL)
    database = models.CharField(max_length=30, verbose_name="数据库名称", help_text="数据库名称")
    user = models.CharField(max_length=30, verbose_name="用户", help_text="用户")
    port = models.IntegerField(verbose_name="端口",help_text="端口")
    password = models.CharField(max_length=30, verbose_name="数据库密码", help_text="数据库密码")
    host = models.CharField(max_length=30, verbose_name="地址", help_text="地址")
    charset = models.CharField(max_length=30, verbose_name="编码", help_text="编码")
    add_time = models.DateTimeField(default=datetime.datetime.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = '开启任务信息'
        verbose_name_plural = '开启任务信息'


class SeleTable(models.Model):
    taskid = models.IntegerField(verbose_name="任务id", default=0, help_text="任务id")
    username = models.ForeignKey(UserProfile, related_name='seletable',null=True, blank=True,verbose_name="登陆账号名称", on_delete=models.SET_NULL)
    seletable = models.CharField(max_length=200, verbose_name="选择表的名称", help_text="选择表的名称")

    class Meta:
        verbose_name = '归档目标表'
        verbose_name_plural = '归档目标表'


class SeleField(models.Model):
    taskid = models.IntegerField(verbose_name="任务id", default=0, help_text="任务id")
    username = models.ForeignKey(UserProfile, related_name='selefield', null=True, blank=True, verbose_name="登陆账号名称", on_delete=models.SET_NULL)
    selefield = models.CharField(max_length=200, verbose_name="选择字段的名称", help_text="选择字段的名称")
    rangetop = models.CharField(max_length=200, null=True, blank=True,verbose_name="过滤上限范围的名称", help_text="过滤上限范围的名称")    # 范围设置为字符串类型方便以后扩展更多字段
    rangelow = models.CharField(max_length=200, null=True, blank=True,verbose_name="过滤下线范围的名称", help_text="过滤下线范围的名称")
    class Meta:
        verbose_name = '归档目标字段'
        verbose_name_plural = '归档目标字段'


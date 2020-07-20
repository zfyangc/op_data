from django.db import models

# Create your models here.





from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """用户"""
    name = models.CharField(max_length=30,null=True,blank=True,verbose_name='姓名')
    position = models.DateField(null=True,blank=True,verbose_name='职位')
    # gender = models.CharField(max_length=6,choices=(("male",u"男"),("female",u'女')),default='男')
    mobile= models.CharField(null = True,blank=True,max_length=11,verbose_name='电话')
    email = models.CharField(max_length=30,null=True,blank=True,verbose_name='邮箱')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

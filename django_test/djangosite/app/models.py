#-*-coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models#所有的django模型类必须继承自他
# Create your models here.

#新增元祖用于设置消息类型枚举项
KIND_CHOICES=(
    ('python技术','python技术'),
    ('数据库技术','数据库技术'),
    ('经济学','经济学'),
    ('文体咨询','文体咨询'),
    ('其他','其他')
)
class Moment(models.Model):
    content=models.CharField(max_length=200)
    user_name=models.CharField(max_length=20,default='匿名')
    kind=models.CharField(max_length=20,choices=KIND_CHOICES,default=KIND_CHOICES[0])

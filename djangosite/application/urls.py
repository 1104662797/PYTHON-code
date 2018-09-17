#!/usr/bin/env python
#_*_ coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^(\d+)$',views.show)#匹配多个数字并获取匹配到的数字,会传回去
]
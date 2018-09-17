#!/usr/bin/env python
#_*_ coding:utf-8 -*-

#路由映射文件
from django.conf.urls import url
from . import views
#关键变量
urlpatterns=[
    url(r'moments_input', views.moments_input),
    url(r'hello',views.hello,name="hello"),
    url(r'',views.welcome,name="welcome"),

]
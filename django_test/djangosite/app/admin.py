#-*-coding:utf-8 -*-
from django.contrib import admin
from .models import Moment
# Register your models here.

class MomentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('消息内容',{
            'fields':('content','kind')
        }),
        ('用户信息',{
            'fields':('user_name',),
        }),
    )
admin.site.register(Moment,MomentAdmin)
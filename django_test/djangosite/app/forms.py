#!/usr/bin/env python
#_*_ coding:utf-8 -*-

from django.forms import ModelForm,ValidationError #diango表单类的基类
from app.models import Moment#引入models.py中定义的Moment

class MomentForm(ModelForm):
    class Meta:
        model=Moment
        fields='__all__'
    def clean(self):
        cleaned_data=super(MomentForm,self).clean()
        content=cleaned_data.get("content")
        if content is None:
            raise ValidationError("重新输入")
        elif content.find("ABCD")>=0:
            raise ValidationError("不能输入敏感字ABCD")
        return cleaned_data
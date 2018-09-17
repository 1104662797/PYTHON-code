from django.contrib import admin
from .models import *
# Register your models here.

class HeroInfoInine(admin.StackedInline):#嵌入heroinfo
    model = HeroInfo
    extra = 1

class BookInfoAdmin(admin.ModelAdmin):
    inlines = [HeroInfoInine]#关联内嵌
    list_display = ['id','bpub_date']
    list_per_page = 1
    fieldsets = [
        ('basic',{'fields':['bittle']}),
        ('time',{'fields':['bpub_date']}),
    ]


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)

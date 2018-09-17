
from django.db import models
# Create your models here.
#我们的类继承自model类还可以作为一个模型类，与数据产生链接
class BookInfo(models.Model):
    bittle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField()
    def __str__(self):
        return self.bittle
class HeroInfo(models.Model):
    hname=models.CharField(max_length=20)
    hgender=models.BooleanField()
    hcontent=models.CharField(max_length=1000)
    hbook=models.ForeignKey('BookInfo',on_delete=models.CASCADE)#定义外键

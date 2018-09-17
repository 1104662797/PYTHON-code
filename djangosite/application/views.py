from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
from .models import *
# Create your views here.

def index(request):
    # temp=loader.get_template('application/index.html')
    # return HttpResponse(temp.render())
    booklist=BookInfo.objects.all()
    context={'list':booklist}#向模板传递数据，以替代模型中的值
    return render(request,'application/index.html',context)
def show(request,id):
    book=BookInfo.objects.get(pk=id)
    herolist=book.heroinfo_set.all()
    context={'list':herolist}
    return render(request,'application/show.html',context)
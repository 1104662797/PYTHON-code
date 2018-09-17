from django.shortcuts import render
from django.http import HttpResponse
import os
from app.forms import MomentForm
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from app import views
# Create your views here.

def welcome(request):
    return HttpResponse("<h1>hello django</h1>")
def hello(request):
    print("_______________*___________________________")
    return HttpResponseRedirect(reverse("welcome"))

def moments_input(request):
    if request.method=='POST':
        form=MomentForm(request.POST)
        if form.is_valid():
            moment=form.save()
            moment.save()
            return HttpResponseRedirect(reverse(views.welcome))
            # url_s=reverse("app.views.welcome")
            # print(url_s)
            # return HttpResponseRedirect(url_s)

    else:
        form=MomentForm()
    PROJECT_ROOT=os.path.dirname(os.path.abspath('moments_input.html'))
    return render(request,os.path.join(PROJECT_ROOT,'app/templates',
                                       'moments_input.html'),{'form':form})

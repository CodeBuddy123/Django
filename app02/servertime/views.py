from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def timedisplay(request):
    dt=datetime.datetime.now()
    msg="<h1 style='color:red'>Hello User!</h1>"
    msg=msg+" <h2 style='color:blue'>Now the time is:"+str(dt)+"</h2>"
    return HttpResponse(msg)

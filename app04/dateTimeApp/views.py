from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def datetimeInfo(request):
    date=datetime.datetime.now()  #getting the current date and time
    h=int(date.strftime("%H"))         #getting only hours from time
    msg="<h1 style='color:red'>Hello User!! Very"
    if(h<12):
        msg=msg+" Good Morning!"+"</h1>"
    elif(h<16):
        msg=msg+" Good Afternoon!"+"</h1>"
    elif(h<21):
        msg=msg+" Good Evening!"+"</h1>"
    else:
        msg=msg+"Good Night!"+"</h1>"

    return HttpResponse(msg)

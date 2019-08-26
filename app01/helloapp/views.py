from django.shortcuts import render
from django.http import HttpResponse

def wish(request):
    msg="<h1 style='color:green'>Hello World! from Django Web Application<h1>"
    return HttpResponse(msg)

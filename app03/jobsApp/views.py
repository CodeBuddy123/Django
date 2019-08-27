from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# defining multiple view functions in single application
def hydjobsinfo(request):
    msg="<h1 style='color:red'>Hyderabad Jobs Information Page</h1>"
    return HttpResponse(msg)

def punejobsinfo(request):
    msg="<h1 style='color:green'>Pune Jobs Information Page</h1>"
    return HttpResponse(msg)

def delhijobsinfo(request):
    msg="<h1 style='color:blue'>Delhi Jobs Information Page</h1>"
    return HttpResponse(msg)

def chennaijobsinfo(request):
    msg="<h1 style='color:brown'>Chennai Jobs Information Page</h1>"
    return HttpResponse(msg)

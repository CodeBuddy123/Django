from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def wish(request):
    msg="<h1 style='color:green'>This is from first Application</h1>"
    return HttpResponse(msg)

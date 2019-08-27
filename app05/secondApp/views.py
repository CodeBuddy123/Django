from django.shortcuts import render
from django.http import HttpResponse

def wish(request):
    msg="<h1 style='color:brown'>This is from second application</h1>"
    return HttpResponse(msg)

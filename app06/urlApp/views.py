from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobsinfo(request):
    msg="<h1 style='color:red'>Hyd Jobs page</h1>"
    return HttpResponse(msg)


def punejobsinfo(request):
    msg="<h1 style='color:blue'>Pune Jobs page</h1>"
    return HttpResponse(msg)

from django.contrib import admin
from django.urls import path
from urlApp import views

urlpatterns = [
    path('punejobs/',views.punejobsinfo ),
    path('hydjobs/',views.hydjobsinfo)
]

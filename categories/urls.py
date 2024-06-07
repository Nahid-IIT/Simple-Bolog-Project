
from django.contrib import admin
from django.urls import path, include
from categories.views import addCategory
urlpatterns = [
     path('add/', addCategory, name = "addCategory"),
    
]

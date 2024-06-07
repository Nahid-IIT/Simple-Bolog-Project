
from django.contrib import admin
from django.urls import path, include
from authors.views import register,userLogin,profile,userLogout,password_change,update_profile
urlpatterns = [
     path('register/', register, name ="register"),
     path('login/', userLogin, name ="userLogin"),
     path('profile/', profile, name ="profile"),
     path('update_profile/', update_profile, name ="update_profile"),
     path('logout/', userLogout, name ="logout"),
     path('password_change/', password_change, name ="password_change"),
]

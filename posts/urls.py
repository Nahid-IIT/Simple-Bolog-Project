
from django.contrib import admin
from django.urls import path
from posts.views import addPost,editPost,deletePost
urlpatterns = [
    path('add/', addPost, name = "addPost"),
    path('edit/<int:id>', editPost, name = "editPost"),
    path('delete/<int:id>', deletePost, name = "deletePost"),
]

# tasks/urls.py

from django.urls import path
from .views import index, delete_task

urlpatterns = [
    path("", index),
    path("delete/<int:index>/", delete_task),
]
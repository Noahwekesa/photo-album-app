# example/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("addphoto/", views.addPhoto, name="add-photo"),
    path("viewphoto/<str:slug>", views.viewPhoto, name="view-photo"),
]

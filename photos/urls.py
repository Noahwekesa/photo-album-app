# example/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("addphoto/", views.add_photo, name="add_photo"),
    path("photo/<slug:slug>/", views.view_photo, name="view_photo"),
]

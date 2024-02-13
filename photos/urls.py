# example/urls.py
from django.urls import path

from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("addphoto/", views.addPhoto, name="add-photo"),
    path("viewphoto/<str:slug>", views.viewPhoto, name="view-photo"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("profile", views.profile, name="profile"),
]

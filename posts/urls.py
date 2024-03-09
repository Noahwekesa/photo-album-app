from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("posts/create/", views.create_posts, name="create_posts"),
    path("posts/<slug:slug>/", views.post_detail_view, name="detail"),
]

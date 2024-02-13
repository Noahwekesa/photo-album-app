from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Category, Photo


def index(request):
    photos = Photo.objects.all().order_by("-created_at")
    context = {"photos": photos}
    return render(request, "index.html", context)


@login_required
def profile(request):
    context = {}
    return render(request, "profile", context)


@login_required
def addPhoto(request):
    context = {}
    return render(request, "add.html", context)


def viewPhoto(request, pk):
    context = {}
    return render(request, "view_photo.html", context)

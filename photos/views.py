from django.shortcuts import render
from .models import Photo


def index(request):
    photos = Photo.objects.all().order_by("-created_at")
    context = {}
    return render(request, "index.html", context)


def addPhoto(request):
    context = {}
    return render(request, "add.html", context)


def viewPhoto(request, pk):
    context = {}
    return render(request, "view_photo.html", context)

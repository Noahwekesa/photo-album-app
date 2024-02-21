from django.contrib.auth.decorators import login_required
from django.shortcuts import Http404, get_object_or_404, render
from .models import Photo


def index(request):
    photos = Photo.objects.all().order_by("-created_at")
    context = {"photos": photos}
    return render(request, "index.html", context)


@login_required
def addPhoto(request):
    context = {}
    return render(request, "add.html", context)


def viewPhoto(request, slug):
    photo = get_object_or_404(Photo, slug=slug)
    context = {"photo": photo}
    return render(request, "photo.html", context)

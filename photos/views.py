from django.contrib.auth.decorators import login_required
from django.shortcuts import Http404, render
from .models import Photo


def index(request):
    photos = Photo.objects.all().order_by("-created_at")
    context = {"photos": photos}
    return render(request, "index.html", context)


@login_required
def profile(request):
    context = {}
    return render(request, "accounts/profile.html", context)


@login_required
def addPhoto(request):
    context = {}
    return render(request, "add.html", context)


def viewPhoto(request, slug):
    photo_obj = None
    if slug is not None:
        try:
            photo_obj = Photo.objects.get(slug=slug)
        except Photo.DoesNotExist:
            raise Http404
        except Photo.MultipleObjectsReturned:
            photo_obj = Photo.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {"object": photo_obj}
    return render(request, "view_photo.html", context)

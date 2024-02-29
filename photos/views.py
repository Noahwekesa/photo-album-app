from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from .forms import AddPhotoForm
from django.contrib import messages


def index(request):
    photos = Photo.objects.all()
    context = {"photos": photos}
    return render(request, "index.html", context)


@login_required
def add_photo(request):
    form = AddPhotoForm()
    if request.method == 'POST':
        form = AddPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.save()
            messages.success(request, 'Photo Posted successfully')
            return redirect('index')
    context = {"form": form}
    return render(request, "photos/add_photo.html", context)


def view_photo(request, slug):
    photo = get_object_or_404(Photo, slug=slug)
    context = {"photo": photo}
    return render(request, "photos/photo_details.html", context)

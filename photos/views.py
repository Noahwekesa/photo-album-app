from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo, Category
from .forms import AddPhotoForm
from django.contrib import messages


def index(request):
    photos = Photo.objects.all()
    context = {"photos": photos}
    return render(request, "index.html", context)


@login_required
def add_photo(request):
    user = request.user
    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new']
            )
        else:
            category = None
        for image in images:
            photo = Photo.objects.create(
                category=category, description=data['description'], image=image,)
        return redirect('index')
    context = {'categories': categories}
    return render(request, "photos/add_photo.html", context)


def view_photo(request, slug):
    photo = get_object_or_404(Photo, slug=slug)
    context = {"photo": photo}
    return render(request, "photos/photo_details.html", context)

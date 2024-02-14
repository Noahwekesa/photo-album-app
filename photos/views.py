from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Category, Photo
from .forms import SignUpForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout


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


def viewPhoto(request, pk):
    context = {}
    return render(request, "view_photo.html", context)


# register users
def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect("login")
    else:
        form = SignUpForm()
        return render(request, "accounts/register.html", {"form": form})

    return render(request, "accounts/register.html", {"form": form})


# logout users
def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out successfully")
    return redirect("login")

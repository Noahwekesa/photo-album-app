from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

from django.contrib import messages
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
            messages.success(request, "Registration successfully")
            return redirect("login")
    else:
        form = SignUpForm()
        return render(request, "accounts/register.html", {"form": form})

    return render(request, "accounts/register.html", {"form": form})


@login_required
def profile(request):
    context = {}
    return render(request, "accounts/profile.html", context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm(request)
    context = {"form": form}
    return render(request, "accounts/login.html", context)


# logout users
def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out successfully")
    return redirect("login")

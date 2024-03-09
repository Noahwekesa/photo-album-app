from django.shortcuts import (
    render,
    redirect,
)
from django.contrib import messages
from .forms import PostCreationForm
from posts.models import Post


def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "index.html", context)


def create_posts(request):
    form = PostCreationForm()
    if request.method == "POST":
        form = PostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Post submitted Successfully!")
            return redirect("index")
    context = {"form": form}
    return render(request, "posts/create_posts.html", context)

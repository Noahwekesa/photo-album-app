from django.shortcuts import (
    get_object_or_404,
    render,
    redirect,
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostCreationForm
from posts.models import Post


def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "index.html", context)


@login_required
def create_posts(request):
    form = PostCreationForm()
    if request.method == "POST":
        form = PostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Post submitted Successfully!")
            return redirect("index")
    else:
        messages.warning(request, "Something went wrong")
    context = {"form": form}
    return render(request, "posts/create_posts.html", context)


def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {"post": post}
    return render(request, "posts/detail.html", context)


def post_delete_view(request, slug):
    pass

from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.fields import AutoSlugField


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=150, unique=True, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"


class Photo(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    Category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    slug = AutoSlugField(populate_from="title")
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

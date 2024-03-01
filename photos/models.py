from django.conf import settings
from django.db import models
import uuid
from django.contrib.auth.models import User

from django_extensions.db.fields import AutoSlugField

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    name = models.CharField(
        max_length=150,
        unique=True,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.name}"


class Photo(models.Model):
    id = models.CharField(
        max_length=100,
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    slug = AutoSlugField(populate_from="title")
    image = models.ImageField(
        blank=False,
        null=False,
    )
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

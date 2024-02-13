from django.contrib import admin

from photos.models import Category, Photo


admin.site.register(Photo)
admin.site.register(Category)

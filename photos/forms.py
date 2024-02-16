from django import forms
from .models import Photo


class AddPhotoForm(forms.Form):
    class Meta:
        models = Photo
        fields = (
            "title",
            "description",
        )

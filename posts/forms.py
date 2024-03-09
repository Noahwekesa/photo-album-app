from django import forms
from .models import Post


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "image",
            "title",
            "description",
        ]
        labels = {"description": "Caption"}
        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Write a caption...",
                    "class": "form-control",
                }
            )
        }

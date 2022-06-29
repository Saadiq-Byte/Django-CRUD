from dataclasses import field
from django import forms

from .models import BlogApp

class BlogAppForm(forms):
    class meta:
        model = BlogApp
        field = [
            "title",
            "description"
        ]
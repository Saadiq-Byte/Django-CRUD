from cgitb import html
from pyexpat import model
from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import BlogApp

class BlogAppCreatview (CreateView):

    model = BlogApp
    fields = [
        "title",
        "description"
    ]

    template_name = 'home.html'

    class BlogApplistview(ListView):
    model = BlogApp
    template_name = 'list.html'

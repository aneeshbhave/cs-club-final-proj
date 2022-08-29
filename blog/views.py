from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class BlogView(generic.DetailView):
    model = Post
    template_name = "blog.html"

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-date")
    template_name = "index.html"

class AboutView(generic.TemplateView):
    template_name = "about.html"

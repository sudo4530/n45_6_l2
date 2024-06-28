from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def blog_post_list(request):
    all_data = Post.objects.all()
    context = {"data": all_data}
    return render(request, "blog.html", context=context)
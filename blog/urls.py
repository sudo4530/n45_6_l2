from django.urls import path
from .views import home, login, register, blog_post_list

urlpatterns = [
    path('', home, name='home'),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("blog/", blog_post_list, name="post")
]
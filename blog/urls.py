from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from .views import PostsView, ShowPost, CreatePost, CategoryView, RegisterUser, LoginUser, logout_user


app_name = "blog"
urlpatterns = [
    path("", cache_page(60)(PostsView.as_view()), name="index"),
    path("create", CreatePost.as_view(), name="create_post"),
    path("post/<slug:post_slug>", ShowPost.as_view(), name="show_post"),
    path("cat/<slug:cat_slug>", cache_page(60)(CategoryView.as_view()), name="show_cat"),
    path("register", RegisterUser.as_view(), name="register"),
    path("login", LoginUser.as_view(), name="login"),
    path("logout", logout_user, name="logout"),
]

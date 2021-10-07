from django.urls import path

from .views import PostsView, ShowPost, CreatePost, CategoryView, RegisterUser, LoginUser, UserProfile, UserLogout

app_name = "blog"
urlpatterns = [
    path("", PostsView.as_view(), name="index"),
    path("create/", CreatePost.as_view(), name="create_post"),
    path("post/<slug:post_slug>", ShowPost.as_view(), name="show_post"),
    path("cat/<slug:cat_slug>", CategoryView.as_view(), name="show_cat"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path("personal-account/<int:pk>", UserProfile.as_view(), name="personal_account"),
]

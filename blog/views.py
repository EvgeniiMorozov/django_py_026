from django.contrib.auth import get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from .forms import PostForm, LoginUserForm, RegisterUserForm
from .models import PostModel
from .utils import DataMixin


# user = get_user_model()


class PostsView(DataMixin, ListView):
    model = PostModel
    template_name = "blog/index.html"
    context_object_name = "posts"

    # extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # user_context = self.get_user_context(text="Главная страница")
        # context.update(user_context)
        context |= self.get_user_context(title="Главная страница")
        return context

    def get_queryset(self):
        return PostModel.objects.filter(is_published=True)


class CategoryView(DataMixin, ListView):
    model = PostModel
    template_name = "blog/index.html"
    context_object_name = "posts"
    # extra_context = {'title': 'Главная страница'}
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= self.get_user_context(title=f"Категория {context['posts'][0].category.name}")

        return context

    def get_queryset(self):
        return PostModel.objects.filter(category__slug=self.kwargs["cat_slug"])


# Slug
class ShowPost(DetailView):
    model = PostModel
    template_name = "blog/show_post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"


class CreatePost(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = "blog/create.html"


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "blog/register.html"
    success_url = reverse_lazy("blog:index")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= self.get_user_context(title="Регистрация")
        return context


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "blog/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= self.get_user_context(title="Вход на сайт")
        return context

    def get_success_url(self):
        return reverse_lazy("blog:index")


# def logout_user(request):
#     logout(request)
#     return redirect("blog:index")


class UserLogout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("blog:index")


class UserProfile(DataMixin, LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        print(request.user.get_username())
        return render(
            request, "blog/personal_account.html", {"user": User.objects.get(username=request.user.get_username())}
        )


# class UserProfile(DataMixin, LoginRequiredMixin, DetailView):
#     model = User
#     template_name = "blog/personal_account.html"
#     # slug_url_kwarg =
#     # pk_url_kwarg = "user_id"
#     context_object_name = "user"

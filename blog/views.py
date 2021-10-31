import logging

from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import PostModel, Category
from .forms import PostForm, RegisterUserForm, LoginUserForm
from .utils import DataMixin

logger = logging.getLogger(__name__)


class PostsView(DataMixin, ListView):
    model = PostModel
    template_name = "blog/index.html"
    context_object_name = "posts"

    # extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # user_context = self.get_user_context(title='Главная страница')
        # context.update(user_context)
        logger.warning("Warning Hello!")
        logger.critical("ПРИВЕТ")
        context |= self.get_user_context(title="Главная страница")
        return context

    def get_queryset(self):
        # return PostModel.objects.filter(is_published=True)
        return PostModel.objects.all().select_related("category")


class CategoryView(DataMixin, ListView):
    model = PostModel
    template_name = "blog/index.html"
    context_object_name = "posts"
    # extra_context = {'title': 'Главная страница'}
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Category.objects.get(slug=self.kwargs["cat_slug"])
        # context |= self.get_user_context(title=f'Категория {context["posts"][0].category.name}')
        context |= self.get_user_context(title=f"Категория {cat.name}")
        return context

    def get_queryset(self):
        return PostModel.objects.filter(category__slug=self.kwargs["cat_slug"]).select_related("category")


# Slug
class ShowPost(DataMixin, DetailView):
    model = PostModel
    template_name = "blog/show_post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= self.get_user_context(title=context["post"].title)
        return context


class CreatePost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = PostForm
    template_name = "blog/create.html"
    raise_exception = False
    login_url = reverse_lazy("blog:login")
    success_url = reverse_lazy("blog:create_post")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= self.get_user_context(title="Создание поста")
        return context


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


def logout_user(request):
    logout(request)
    return redirect("blog:index")


class UserProfile:
    pass


class LoadMorePosts(View):
    def get(self, request, *args, **kwargs):
        last_post_id = request.GET.get("lastPostId")
        print(last_post_id)
        posts = PostModel.objects.filter(pk__lt=int(last_post_id)).order_by("-publish_date", "title")[:3]
        print(posts)

        if not posts:
            return JsonResponse({"data": False})

        data = []

        for post in posts:
            obj = {
                "id": post.id,
                "author": post.author,
                "title": post.title,
                "text": post.text,
                "image_url": post.image.url,
                "publish_date": post.publish_date,
                "cat_name": post.category.name,
                "cat_url": f"cat/{post.category.slug}",
                "post_url": f"post/{post.slug}",
            }
            data.append(obj)
        data[-1]["last_post"] = True
        return JsonResponse({"data": data})

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import PostForm
from .models import PostModel
from .utils import DataMixin


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
    form_class = UserCreationForm
    template_name = "blog/register.html"
    success_url = reverse_lazy("blog:index")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= self.get_user_context(title="Регистрация")


class LoginUser:
    pass

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import PostModel
from .forms import PostForm


class PostsView(ListView):
    model = PostModel
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    # extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return PostModel.objects.filter(is_published=True)


class CategoryView(ListView):
    model = PostModel
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    # extra_context = {'title': 'Главная страница'}
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return PostModel.objects.filter(category__slug=self.kwargs['cat_slug'])


# Slug
class ShowPost(DetailView):
    model = PostModel
    template_name = 'blog/show_post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


class CreatePost(CreateView):
    form_class = PostForm
    template_name = 'blog/create.html'

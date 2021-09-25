from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from blog.models import PostModel
from .forms import PostForm


# def index(request):
#     posts = PostModel.objects.all()
#     context = {
#         'posts': posts
#     }
#     return render(request, 'blog/index.html', context)


class PostsView(ListView):
    model = PostModel
    template_name = "blog/index.html"
    context_object_name = "posts"
    extra_content = {"title": "Main page"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return PostModel.objects.filter(is_published=True)


class ShowPost(DetailView):
    model = PostModel
    pk_url_kwarg = "id"
    context_object_name = "post"


class CreatePost(CreateView):
    form_class = PostForm
    template_name = "blog/create.html"

    def get_success_url(self):
        return reverse_lazy('blog:index')


# def create_post(request):
#     # if request.method == 'POST':
#     #     post = PostModel(
#     #         author=request.POST.get('authorArticle'),
#     #         title=request.POST.get('titleArticle'),
#     #         text=request.POST.get('textArticle')
#     #     )
#     #     post.save()
#     error = ""
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             redirect("blog:index")
#         else:
#             error = "Данные формы не корректны!"

#     form = PostForm()
#     context = {"form": form, "error": error}
#     return render(request, "blog/create.html", context)

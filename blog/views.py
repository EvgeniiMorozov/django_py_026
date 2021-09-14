from django.shortcuts import render, redirect

from blog.models import PostModel
from .forms import PostForm


def index(request):
    posts = PostModel.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def create_post(request):
    # if request.method == 'POST':
    #     post = PostModel(
    #         author=request.POST.get('authorArticle'),
    #         title=request.POST.get('titleArticle'),
    #         text=request.POST.get('textArticle')
    #     )
    #     post.save()
    error = ''
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("blog:index")
        else:
            error = "Данные формы не корректны!"

    form = PostForm()
    context = {
        'form': form,
        "error": error
    }
    return render(request, 'blog/create.html', context)

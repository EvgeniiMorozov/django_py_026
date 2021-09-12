from django.shortcuts import render

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
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'blog/create.html', context)

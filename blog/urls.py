from django.urls import path

from . import views
from .views import CreatePost, PostsView, ShowPost

app_name = 'blog'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', PostsView.as_view(), name='index'),
    path('post/<int:id>', ShowPost.as_view(), name='show_post'),
    # path('create', views.create_post, name='create_post'),
    path('create', CreatePost.as_view(), name='create_post'),
]

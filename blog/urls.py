from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_post, name='create_post'),
    # path('about', views.about),
    # path('create', views.create_product),
    # path('delete/<int:prod_id>', views.delete_product),
    # path('buy/<int:prod_id>', views.buy_product),
]

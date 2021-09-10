from cloudipsp import Api, Checkout
from django.shortcuts import render, redirect

from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'shop_app/index.html', {'products': products})


def about(request):
    return render(request, 'shop_app/about.html')


def create_product(request):
    if request.method == 'POST':
        product = Product(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            price=request.POST.get('price'),
        )
        product.save()

    return render(request, 'shop_app/create.html')


def delete_product(request, prod_id):
    Product.objects.filter(id=prod_id).delete()
    return redirect('shop_app:index')


def buy_product(request, prod_id):
    product = Product.objects.get(id=prod_id)
    api = Api(merchant_id=1396424, secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "RUB",
        "amount": str(product.price) + '00'
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponse, HttpRequest

from .models import Category, Product
# Create your views here.


def show_product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {"category": category, 'categories': categories, 'products': products})


def product_info(request, id, slug):
    product = get_object_or_404(Category, slug=slug, id=id, available=True)
    return render(request, 'shop/product/info.html', {'product': product})

# def test(request, var):
#     if request.method == 'POST':
#         print('пост запрос')
#         print(HttpRequest.META['CONTENT-LENGTH'])
#         print(HttpRequest.headers)
#     if request.method == 'GET':
#         print('гет запрос')
#     if var:
#         return HttpResponse('<h1>Страница найдена</h1>')
#     return HttpResponseNotFound('<h1>404 error</h1>')

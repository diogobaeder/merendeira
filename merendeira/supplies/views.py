from django.shortcuts import render
from django.http import Http404

from merendeira.supplies.models import Category, Product


def list_categories(request):
    categories = Category.objects.all()

    return render(request, 'supplies/categories.html', {
        'categories': categories,
    })


def list_products(request, slug):
    products = Product.objects.filter(category__slug=slug)
    if not products:
        raise Http404('No products found.')

    return render(request, 'supplies/products.html', {
        'products': products,
    })

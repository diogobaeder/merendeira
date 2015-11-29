from django.shortcuts import render

from merendeira.supplies.models import Category


def list_categories(request):
    categories = Category.objects.all()

    return render(request, 'categories.html', {
        'categories': categories,
    })

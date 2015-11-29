from django.test import TestCase
from nose.tools import istest

from merendeira.supplies.models import Category


class CategoryViewTest(TestCase):
    @istest
    def lists_categories(self):
        category1 = Category.objects.create(title='Comidas')
        category2 = Category.objects.create(title='Bebidas')

        response = self.client.get('/mantimentos/categorias')

        self.assertContains(response, category1.title)
        self.assertContains(response, category2.title)

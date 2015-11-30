from django.test import TestCase
from nose.tools import istest

from merendeira.supplies.models import Category, Product


class CategoryViewTest(TestCase):
    @istest
    def lists_categories(self):
        category1 = Category.objects.create(title='Comidas')
        category2 = Category.objects.create(title='Bebidas')

        response = self.client.get('/mantimentos/categorias')

        self.assertContains(response, category1.title)
        self.assertContains(response, category2.title)


class ProductViewTest(TestCase):
    def create_category(self):
        return Category.objects.create(title='Comidas')

    @istest
    def lists_products(self):
        category = self.create_category()
        product1 = Product.objects.create(title='Tomate', category=category)
        product2 = Product.objects.create(title='Alface', category=category)

        response = self.client.get('/mantimentos/{}'.format(category.slug))

        self.assertContains(response, product1.title)
        self.assertContains(response, product2.title)

    @istest
    def cannot_list_products_if_category_doesn_exist(self):
        response = self.client.get('/mantimentos/navios')

        self.assertEqual(response.status_code, 404)

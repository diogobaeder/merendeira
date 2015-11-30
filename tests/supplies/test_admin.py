from model_mommy import mommy
from django.contrib.auth.models import User
from django.test import TestCase
from nose.tools import istest

from merendeira.supplies.models import Category, Product


class AdminTestCase(TestCase):
    def setUp(self):
        super().setUp()
        password = 'somepass'
        user = User.objects.create_superuser(
            'johndoe', 'johndoe@example.com', password)
        self.client.login(username=user.username, password=password)


class CategoryAdminTest(AdminTestCase):
    @istest
    def is_listed_in_admin(self):
        category = Category.objects.create(title='Comidas')

        response = self.client.get('/admin/supplies/category/')

        self.assertContains(response, category.title)


class ProductAdminTest(AdminTestCase):
    def create_category(self):
        return Category.objects.create(title='Comidas')

    @istest
    def is_listed_in_admin(self):
        product = Product.objects.create(
            title='Tomate', category=self.create_category())

        response = self.client.get('/admin/supplies/product/')

        self.assertContains(response, product.title)

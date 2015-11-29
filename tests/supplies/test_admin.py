from model_mommy import mommy
from django.contrib.auth.models import User
from django.test import TestCase
from nose.tools import istest

from merendeira.supplies.models import Category


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

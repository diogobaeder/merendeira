from django.test import TestCase
from nose.tools import istest

from merendeira.supplies.models import Category


class CategoryTest(TestCase):
    @istest
    def creates_a_basic_instance(self):
        Category.objects.create(
            title='Comidas',
        )

        category = Category.objects.get(pk=1)

        self.assertEqual(category.title, 'Comidas')
        self.assertEqual(category.slug, 'comidas')

    @istest
    def is_printable_by_title(self):
        category = Category.objects.create(
            title='Comidas',
        )

        self.assertEqual(str(category), 'Comidas')

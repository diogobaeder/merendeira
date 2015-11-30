from django.db import models
from mezzanine.core.models import Displayable


class Category(Displayable):
    class Meta:
        verbose_name_plural = 'Categories'


class Product(Displayable):
    category = models.ForeignKey(Category)

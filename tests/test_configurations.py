from django.test import TestCase
from nose.tools import istest


class ConfigurationsTest(TestCase):
    @istest
    def loads_settings(self):
        try:
            from django.conf import settings
        except Exception as e:
            self.fail(e.message)

from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url('categorias', 'merendeira.supplies.views.list_categories',
        name='mantimentos-categorias'),
    url('(?P<slug>.+)', 'merendeira.supplies.views.list_products',
        name='mantimentos-produtos'),
)

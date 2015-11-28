test:
	DJANGO_SETTINGS_MODULE=merendeira.test_settings python manage.py test

testing:
	export PYTHONPATH=$PWD/merendeira/
	export DJANGO_SETTINGS_MODULE=merendeira.test_settings

build: test lint

test:
	DJANGO_SETTINGS_MODULE=merendeira.test_settings python manage.py test

lint:
	flake8 merendeira

testing:
	export PYTHONPATH=$PWD/merendeira/
	export DJANGO_SETTINGS_MODULE=merendeira.test_settings

freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

migrations:
	DJANGO_SETTINGS_MODULE=merendeira.test_settings python manage.py makemigrations

syncdb:
	python manage.py syncdb

run:
	python manage.py runserver

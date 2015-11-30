build: cover-test lint

test:
	DJANGO_SETTINGS_MODULE=merendeira.test_settings python manage.py test

cover-test:
	DJANGO_SETTINGS_MODULE=merendeira.test_settings coverage run manage.py test
	coverage report -m

lint:
	flake8 merendeira

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

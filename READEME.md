# Django Personal Event Calender

## How To Setup
1. Create a Project Directory `mkdir django_market_todo`
2. Go to Project Directory `cd django_market_todo`
3. Create a Virtual Environment `pip install pipenv`
4. Activate Virtual Environment `pipenv shell`
5. Install Requirements Package `pipenv install -r requirements.txt`
6. Create a New Project `django-admin startproject backend`
7. Go to Backend Project Directory `cd backend`
8. Create a New App `python manage.py startapp todo`
9. Create Migration `python manage.py makemigrations`
10. Migrate Database `python manage.py migrate`
11. Create Super User `python manage.py createsuperuser`
12. Finally Run The Project `python manage.py runserver`
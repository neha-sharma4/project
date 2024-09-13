Create a virtual environment
    
    python -m venv venv

Activate it

    ./venv/Scripts/activate

Install Django

    pip install django

Create the project

    django-admin startproject project .

Create the application

    django-admin startapp main

Add the application to the project in the `project\settings.py` file

Build a model from the `main\models.py`

Make the migrations

    python manage.py makemigrations
    python manage.py migrate

Now create a `main\forms.py` file

Now create a views to the `main\views.py` file          
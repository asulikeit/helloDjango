# helloDjango

### [NOTE] Create project and app

    mkdir HelloDjango
    django-admin startproject djangoapp .
    mkdir -p apps/deals
    django-admin startapp deals apps/deals
    mkdir -p apps/peoples
    django-admin startapp deals apps/peoples

### Requriement: python 3.7

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    (Django==3.2.10, djangorestframework==3.13.1)

### Test

    python manage.py test

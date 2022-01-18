# helloDjango

### [NOTE] Create project and app

    mkdir HelloDjango
    django-admin startproject djangoapp .
    mkdir -p apps/deals
    django-admin startapp deals apps/deals
    mkdir -p apps/peoples
    django-admin startapp peoples apps/peoples
    django-admin startapp commonapi

### Requriement: python 3.7 & sqlite3.dll

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    (Django==3.2.10, djangorestframework==3.13.1)

    Download and replace sqlite3.dll file
    https://code.djangoproject.com/wiki/JSON1Extension

### Test

    python manage.py test

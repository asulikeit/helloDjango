# helloDjango

### [NOTE] Create project and app

    mkdir HelloDjango
    django-admin startproject djangoapp .
    mkdir -p apps/deals
    django-admin startapp deals apps/deals
    mkdir -p apps/peoples
    django-admin startapp peoples apps/peoples
    mkdir -p apps/memberships
    django-admin startapp memberships apps/memberships
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
    
### ERD
![image](https://user-images.githubusercontent.com/8528659/158085014-44d887d1-060b-4d4f-b3f2-9a27b2f8c4e7.png)

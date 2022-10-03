# helloDjango

### TODO

    Django(DRF)의 table join 방법과 serializer 사용법에 대해서 정리하고 있습니다.
    apps/ 하위로 코드를 넣고 있는데 대부분 CRUD 관련이라서
    openapis/ 로 HTTP API 코드를 분리하고 apps/ 는 ORM 처리만 하도록 정리 예정입니다.
    (apps/ 하위의 views.py 파일은 모두 삭제 예정입니다.)
    logics.py 를 추가하여 비즈니스 로직을 넣으려고 하였는데
    DB 종속성이 강하다보니 로직 정리가 쉽지 않아서
    domains.py 를 추가하여 정리 중 입니다.

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

    (NT) Download and replace sqlite3.dll file
    https://code.djangoproject.com/wiki/JSON1Extension

    (CENTOS) Upgrade sqlite3 to 3.9+

### Test

    python manage.py test
    
### ERD
![image](https://user-images.githubusercontent.com/8528659/158085014-44d887d1-060b-4d4f-b3f2-9a27b2f8c4e7.png)

# записать в requirements.txt
'''
Django
djangorestframework
psycopg2-binary # чтобы связываться с postgre
Pillow #чтобы проект мог с картинками работать
'''
# устанавливаем вирт.окружение и активируем
'''
python3 -m venv env
. venv/bin/activate
(venv) py20_shop$ 
'''

# Если не появилось окно, то Ctrl+Shift+P и набрать >python select и выбрать окружение

# Для развертки проекта
'''django-admin startproject <название проекта> .'''

# Появится manage.py, самый главный документ, с помощью которой ведется работа в django

# создаем составные части - приложения (создаются папки)
'''
(env) py20_shop$ python manage.py startapp <название приложения>
(env) py20_shop$ python manage.py startapp <название приложения>
(env) py20_shop$ python manage.py startapp <название приложения>
'''
# создаем БД в postgres
'''
psql -U test_user
test_user # create database shop;
CREATE DATABASE
'''
# добавить в settings.py в папке shop в раздел INSTALLED APP добавленные accounts, products, orders
'''
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts',
    'products',
    'orders'
]
'''
# настроим databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', #django.db.backends.sqlite3
        'NAME': 'shop', #BASE_DIR / 'db.sqlite3',
        'HOST': 'localhost',
        'PORT': 5432,
        'USER': 'test_user', # юзер через которого создали БД
        'PASSWORD': '1'
    }
'''
# настроим язык и timezone
'''
LANGUAGE_CODE = 'en-us' # можно поменять на ru

TIME_ZONE = 'Asia/Bishkek' #'UTC'
'''
# настроим статик и медиа
'''
STATIC_URL = 'static/' #чтобы поддерживать статические файлы
STATIC_ROOT = os.path.join(BASE_DIR, 'static') 
AUTH_USER_MODEL = 'название приложения.название модели'
'''

'''
Email: vealtto@gmail.com
Name: Beknazar
Password: 1234
'''

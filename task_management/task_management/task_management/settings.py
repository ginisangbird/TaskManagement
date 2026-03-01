# task_management/settings.py

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'tasks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'task_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {},
    },
]

WSGI_APPLICATION = 'task_management.wsgi.application'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Can leave empty for app templates
        'APP_DIRS': True,  # MUST be True
        'OPTIONS': {},
    },
]
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'tasks',  # <-- your app
]

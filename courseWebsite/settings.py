"""
Django settings for courseWebsite project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i&to3#n$g0k$hmvvhb9*_&jszk!p^1g9oc=$@(hn=p5hycgr@q'
# SECRET_KEY = os.environ['DJANGO_SECRET']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['yeager.cse.buffalo.edu']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'courses',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'courseWebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'courses.context_processors.all_comments',
                'courses.context_processors.all_courses',
                'courses.context_processors.all_content',
                'courses.context_processors.all_lectures',
                'courses.context_processors.all_assignments',
                'courses.context_processors.syllabus',
                'courses.context_processors.schedule',

            ],
        },
    },
]

WSGI_APPLICATION = 'courseWebsite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': os.environ['DJANGO_DB_NAME'],
    #     'USER': os.environ['DJANGO_DB_USER'],
    #     'PASSWORD': os.environ['DJANGO_DB_KEY'],
    #     'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
    #     'PORT': '3306',
    # }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# STATIC_URL = '/static/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
# STATIC_ROOT = '/http://www.cse.buffalo.edu/~hartloff/CourseWebsite/lecture/'

STATIC_URL = '/static/'
# STATIC_URL = 'http://www.cse.buffalo.edu/~hartloff/CourseWebsite/static/'
# STATIC_URL = 'http://google.com'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
#     '/home/csdue/hartloff/public_html/',
#     '/home/csdue/hartloff/public_html/CourseWebsite/lecture/',
#     '/home/csdue/hartloff/public_html/CourseWebsite/lecture/static/',
#     '/~hartloff/CourseWebsite/lecture/',
# ]

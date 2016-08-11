# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

"""
Django settings for qiime_workshops project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import environ


BASE_DIR = environ.Path(__file__) - 3

env = environ.Env()


DEBUG = env.bool("DJANGO_DEBUG", False)


ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'subdomains',
]

LOCAL_APPS = [
    'payments.apps.PaymentsConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'payments.middleware.PatchedSubdomainURLRoutingMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls.payments'

SUBDOMAIN_URLCONFS = {
    'workshops': 'config.urls.payments',
    'payment-callback': 'config.urls.callback',
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
validator_prefix = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': '%s.UserAttributeSimilarityValidator' % validator_prefix,
    },
    {
        'NAME': '%s.MinimumLengthValidator' % validator_prefix,
    },
    {
        'NAME': '%s.CommonPasswordValidator' % validator_prefix,
    },
    {
        'NAME': '%s.NumericPasswordValidator' % validator_prefix,
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Phoenix'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = str(BASE_DIR('staticfiles'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    str(BASE_DIR.path('static')),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

ADMIN_URL = r'^admin/'

EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.smtp.EmailBackend')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR.path('db.sqlite3')),
    }
}

INTERNAL_IPS = ('127.0.0.1', 'localhost')

SITE_ID = 1

def list_of_tuples(var):
    pairs = var.split(';')
    out = []
    for pair in pairs:
        out.append(tuple(pair.split(',')))
    return out

ADMINS = env('ADMINS', default=list_of_tuples('x,x@x.com;y,y@y.com'),
             cast=list_of_tuples)

# App-specific business logic
LMID = env.str('LMID', '1234')
PAYMENT_URL = env.str('PAYMENT_URL', 'http://www.example.com')
PAYMENT_TITLE = env.str('PAYMENT_TITLE', 'test')
PAYMENT_DESCRIPTION = env.str('PAYMENT_DESCRIPTION', 'test')
PAYMENT_CONTACT_INFO = env.str('PAYMENT_CONTACT_INFO', 'EXAMPLE GROUP\n'
                                                       'example@example.com')
PAYMENT_CERT_BUNDLE = env.str('PAYMENT_CERT_BUNDLE', './static/bundle.pem')
PSF_SPEEDTYPE = env.str('PSF_SPEEDTYPE', '0000')
PSF_ACCT_NUMBER = env.str('PSF_ACCT_NUMBER', '0000')

"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from pathlib import Path

from split_settings.tools import optional, include

from app.conf.environ import env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SECRET_KEY = env('SECRET_KEY', cast=str, default='voj3ep7uw7eje7tyuhff=a5fm_hn2qjgomj$rui42uz-wo!ymukhuf53_b8-)&(*+(')

include(
    'conf/base.py',
    'conf/db.py',
    'conf/installed_apps.py',
    'conf/http.py',
    'conf/middleware.py',
    'conf/templates.py',
    'conf/i18n.py',
    'conf/security.py',
    'conf/static.py',
    optional('conf/local_settings.py'),
)

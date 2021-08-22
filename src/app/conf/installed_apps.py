# Application definition

PROJECT_APPS = [
    'users',
    'categories',
    'products',
    'refs',
    'sellers',
    'buyers',
]

INSTALLED_APPS = [
    'corsheaders',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',

    'rangefilter',
    'django_admin_listfilter_dropdown',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + [app for app in PROJECT_APPS]

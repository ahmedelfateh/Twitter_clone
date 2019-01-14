from .base import *

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', ]

###############
#####-Apps-####
##############


INSTALLED_APPS += [

]


###############
##-Database-##
##############

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEMPLATES_DIRS = os.path.join(BASE_DIR, "templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIRS],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

##################
##-Static files-##
##################

STATIC_URL = '/local-static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_storage"),
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_serve")

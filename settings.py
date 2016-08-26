# Django settings for openeats project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'tk1ig_pa_p9^muz4vw4%#q@0no$=ce1*b$#s343jouyq9lj)k33j('

SITE_ID = 1

ADMINS = (
    # ('Your Name', 'youremail@email.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

AUTH_PROFILE_MODULE = 'accounts.UserProfiles'

# List of callables that know how to import templates from various sources.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_PATH, 'templates'),],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
                'django.core.context_processors.static',
                "navbar.context_processors.navbars",
                "openeats.context_processors.oelogo",
                "openeats.context_processors.oetitle",
            ],
        },
    },
]

TEMPLATE_DIRS = (
   os.path.join(PROJECT_PATH, 'templates'),
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'pagination.middleware.PaginationMiddleware',
    
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

LOCALE_PATHS = (
  os.path.join(BASE_DIR, 'locale',),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.staticfiles',
    'grappelli.dashboard',
    'grappelli',
    'taggit',
    'taggit_templatetags',
    'registration',
    'rosetta',
    'imagekit',
    'haystack',
    'pagination',
    'django_extensions',
    'tastypie',
    'recipe',
    'recipe_groups',
    'ingredient',
    'accounts',
    'news',
    'list',
)

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


ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name

TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'site-media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static-files')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/site-media/'
STATIC_URL = '/static-files/'

ugettext = lambda s: s

LANGUAGES = (
     ('en', ugettext('English')),
     ('de', ugettext('German')),
     ('es', ugettext('Spanish')),
   )



#OpenEats2 Settings
OELOGO = 'images/oelogo.png'
OETITLE = 'OpenEats2 Dev'

#Email Server Settings
DEFAULT_FROM_EMAIL = ''
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT =''
#EMAIL_USE_TLS = True

#registration
LOGIN_REDIRECT_URL = "/recipe/"
ACCOUNT_ACTIVATION_DAYS = 7

#Haystack config
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH':    os.path.join(BASE_DIR, 'search_index')
    }
}


GRAPPELLI_ADMIN_TITLE = OETITLE
GRAPPELLI_INDEX_DASHBOARD = 'openeats.dashboard.CustomIndexDashboard'

PAGINATION_DEFAULT_PAGINATION = 10


try:
    from local_settings import *
except ImportError:
    pass

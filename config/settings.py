from pathlib import Path
import os
from dotenv import load_dotenv
from datetime import timedelta

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-q8k=4$lupv#&q-_9m4^9ukdv=$+)s&fyn^g#xqzxkbn7icm*2)'

DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'olcha',  # Your custom app
    'users',
    'rest_framework',
    'drf_yasg',  # Swagger
    'rest_framework.authtoken',
    'dj_rest_auth',  # Add dj-rest-auth for handling JWT login/logout
    'dj_rest_auth.registration',  # Add registration functionality
    'allauth',  # Allauth for authentication and registration
    'allauth.account',  # Allauth for account management
    'allauth.socialaccount',  # Allauth social account integration (optional)
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Added AccountMiddleware
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": 'postgres',
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": 'localhost',
        "PORT": '5432',
    }
}

# Password validation
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

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static and media files settings
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST framework settings for JWT authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # Use JWT authentication only
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# JWT settings for token expiration
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),  # Access token lifetime
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # Refresh token lifetime
    'ROTATE_REFRESH_TOKENS': False,  # Disable refresh token rotation
    'BLACKLIST_AFTER_ROTATION': False,  # Do not blacklist tokens after rotation
    'AUTH_HEADER_TYPES': ('Bearer',),  # Use Bearer authorization header
}

# Allauth settings
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Default authentication backend
    'allauth.account.auth_backends.AuthenticationBackend',  # Allauth authentication backend
)

# Allauth account settings
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
ACCOUNT_LOGIN_ON_SIGNUP = True
ACCOUNT_LOGOUT_ON_GET = True

# Set the login redirect URL after successful login
LOGIN_REDIRECT_URL = '/'  # Change this to the URL you want to redirect to after login
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_REQUIRED = True
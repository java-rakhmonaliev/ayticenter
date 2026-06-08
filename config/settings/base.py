"""
Base settings for aytimarkaz project.
"""
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config('SECRET_KEY', default='django-insecure-dev-key-change-in-production-12345')

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=lambda v: [s.strip() for s in v.split(',')])

DJANGO_APPS = [
    'unfold',
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'adminsortable2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'core',
    'courses',
    'teachers',
    'admissions',
    'career',
    'news',
    'gallery',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'uz'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = False
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Unfold admin theme
UNFOLD = {
    "SITE_TITLE": "IT Center Yaypan",
    "SITE_HEADER": "IT Center Yaypan",
    "SITE_SUBHEADER": "Boshqaruv paneli",
    "SITE_URL": "/",
    "SITE_SYMBOL": "school",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "COLORS": {
        "primary": {
            "50": "238 238 251",
            "100": "220 220 248",
            "200": "185 184 244",
            "300": "148 146 239",
            "400": "110 108 234",
            "500": "61 59 232",
            "600": "48 46 189",
            "700": "36 34 151",
            "800": "24 23 113",
            "900": "12 11 76",
            "950": "6 5 57",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": "Asosiy",
                "items": [
                    {
                        "title": "Dashboard",
                        "icon": "dashboard",
                        "link": "/admin/",
                    },
                    {
                        "title": "Sayt sozlamalari",
                        "icon": "settings",
                        "link": "/admin/core/sitesettings/",
                    },
                ],
            },
            {
                "title": "Kurslar va O'qituvchilar",
                "items": [
                    {
                        "title": "Kurslar",
                        "icon": "menu_book",
                        "link": "/admin/courses/course/",
                    },
                    {
                        "title": "O'qituvchilar",
                        "icon": "person",
                        "link": "/admin/teachers/teacher/",
                    },
                ],
            },
            {
                "title": "Ariza va Talabalar",
                "items": [
                    {
                        "title": "Arizalar",
                        "icon": "assignment",
                        "link": "/admin/admissions/application/",
                    },
                ],
            },
            {
                "title": "Kontent",
                "items": [
                    {
                        "title": "Yangiliklar",
                        "icon": "newspaper",
                        "link": "/admin/news/post/",
                    },
                    {
                        "title": "Galereya",
                        "icon": "photo_library",
                        "link": "/admin/gallery/photo/",
                    },
                    {
                        "title": "Karyera yo'llari",
                        "icon": "work",
                        "link": "/admin/career/careerpath/",
                    },
                ],
            },
        ],
    },
}

from armstrong.dev.tasks import *


settings = {
    'DEBUG': True,
    'INSTALLED_APPS': (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'armstrong.core.arm_content',
        'armstrong.apps.content',
        'armstrong.apps.articles',
        'south',
        'reversion',
    ),
    'ROOT_URLCONF': 'armstrong.apps.articles.tests.articles_support.urls',
    'SITE_ID': 1,
}

main_app = "articles"
tested_apps = (main_app, )

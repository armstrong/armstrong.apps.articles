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
        'armstrong.core.arm_sections',
        'armstrong.hatband',
        'armstrong.apps.content',
        'armstrong.apps.articles',
        'armstrong.apps.articles.tests.articles_support',
        'south',
        'mptt',
    ),
    'ROOT_URLCONF': 'armstrong.apps.articles.tests.articles_support.urls',
    'SITE_ID': 1,
    'STATIC_URL': '/static/',
}

main_app = "articles"
full_name = "armstrong.apps.articles"
tested_apps = (main_app, 'articles_support')
pip_install_first = True

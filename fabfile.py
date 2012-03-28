from armstrong.dev.tasks import *


settings = {
    'DEBUG': True,
    'INSTALLED_APPS': (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'armstrong.core.arm_access',
        'armstrong.core.arm_content',
        'armstrong.core.arm_sections',
        'armstrong.hatband',
        'armstrong.apps.content',
        'armstrong.apps.articles',
        'south',
        'mptt',
        'taggit',
    ),
    'ROOT_URLCONF': 'armstrong.apps.articles.tests.urls',
    'SITE_ID': 1,
    'STATIC_URL': '/static/',
}

main_app = "articles"
full_name = "armstrong.apps.articles"
tested_apps = (main_app,)
pip_install_first = True

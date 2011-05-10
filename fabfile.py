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
    ),
    'SITE_ID': 1,
}

main_app = "articles"
tested_apps = (main_app, )

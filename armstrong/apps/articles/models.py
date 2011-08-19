from armstrong.apps.content.models import Content
from armstrong.core.arm_content.mixins.publication import PublishedManager
from django.db import models


class Article(Content):
    body = models.TextField()

    objects = models.Manager()
    published = PublishedManager()

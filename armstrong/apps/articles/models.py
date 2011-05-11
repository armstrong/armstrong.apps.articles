from armstrong.apps.content.models import Content
from django.db import models


class Article(Content):
    body = models.TextField()

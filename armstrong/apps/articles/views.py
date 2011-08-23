from django.core.exceptions import ImproperlyConfigured
from django.contrib.syndication.views import Feed

from .models import Article


class ArticleFeed(Feed):
    def __init__(self, title, link, queryset=None, *args, **kwargs):
        self.title = title
        self.link = link
        if queryset is None:
            queryset = Article.objects.all()
        self.queryset = queryset

    def items(self):
        return self.queryset.all()

from django.contrib import admin
from reversion.admin import VersionAdmin

from .models import Article


class ArticleAdmin(VersionAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'summary', 'body', ),
        }),

        # TODO: Refactor this into a common utility function
        ('Publication Information', {
            'fields': ('pub_date', 'pub_status', 'sites', ),
        }),

        # TODO: Refactor this into a fieldset_for(some_model) method so it can
        #       be reused in other apps.
        ('Author Information', {
            'fields': ('authors', 'authors_override', 'authors_extra'),
        }),
    )


admin.site.register(Article, ArticleAdmin)

from django.contrib import admin
from reversion.admin import VersionAdmin

from armstrong.core.arm_content.admin import fieldsets
from .models import Article


class ArticleAdmin(VersionAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'summary', 'body', ),
        }),

        fieldsets.publication(),
        fieldsets.authors(),
    )


admin.site.register(Article, ArticleAdmin)

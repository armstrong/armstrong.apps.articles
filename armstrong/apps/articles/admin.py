from django.contrib import admin
from reversion.admin import VersionAdmin

from armstrong.core.arm_content.admin import fieldsets
from .models import Article


class ArticleAdmin(VersionAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'summary', 'body',
                'primary_section', 'sections', ),
        }),

        fieldsets.PUBLICATION,
        fieldsets.AUTHORS,
    )


admin.site.register(Article, ArticleAdmin)

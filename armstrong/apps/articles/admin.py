from django.contrib import admin
from reversion.admin import VersionAdmin

from armstrong.core.arm_content.admin import fieldsets
from armstrong.core.arm_sections.admin import SectionTreeAdminMixin
from armstrong import hatband
from armstrong.apps.related_content.admin import RelatedContentInline
from .models import Article


class ArticleAdmin(SectionTreeAdminMixin, VersionAdmin, hatband.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'summary', 'body', ),
        }),

        fieldsets.TAXONOMY,
        fieldsets.PUBLICATION,
        fieldsets.AUTHORS,
    )

    inlines = [
        RelatedContentInline,
    ]


admin.site.register(Article, ArticleAdmin)

from django.contrib import admin
from django.utils.html import format_html
from data.models import IndexChange

@admin.register(IndexChange)
class IndexChangeAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="250" height="80" />'.format(obj.background.url))

    image_tag.short_description = 'Image'
    list_display = ['image_tag', 'team', 'title1', 'title2', 'title3',]

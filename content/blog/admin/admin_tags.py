from blog.models.tags import Tags
from django.contrib import admin


@admin.register(Tags)
class AdminTags(admin.ModelAdmin):
    ...
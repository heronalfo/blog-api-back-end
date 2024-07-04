from blog.models.comments import Comments
from django.contrib import admin


@admin.register(Comments)
class AdminComments(admin.ModelAdmin):
    ...
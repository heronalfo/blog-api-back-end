from blog.models.likes import Likes
from django.contrib import admin


@admin.register(Likes)
class AdminLikes(admin.ModelAdmin):
    ...
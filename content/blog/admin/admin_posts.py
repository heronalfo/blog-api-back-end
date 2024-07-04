from blog.models.posts import Posts
from django.contrib import admin


@admin.register(Posts)
class AdminPosts(admin.ModelAdmin):
    ...
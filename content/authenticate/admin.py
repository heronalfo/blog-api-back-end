from django.contrib import admin
from .models import BlogUser

@admin.register(BlogUser)
class AdminBlogUser(admin.ModelAdmin):
    ...
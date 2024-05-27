from django.db import models
from django.contrib.auth.models import User

class BlogUser(models.Model):

    id_user = models.ForeignKey(User, models.CASCADE)
    
    name = models.CharField(max_length=12)
    
    description = models.CharField(max_length=80)
    
    class Meta:
       
        verbose_name = 'blog_user'
        
        verbose_name_plural = 'blog_users'
        
    class Index:
    
        fields = ['name', ]
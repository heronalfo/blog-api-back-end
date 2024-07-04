from django.db import models
from django.contrib.auth.models import User

class BlogUser(models.Model):

    description = models.CharField(max_length=80, default='No bio yet')

    id_user = models.ForeignKey(User, models.CASCADE,  related_name='blog_user')
    
    name = models.CharField(max_length=12)
        
    class Index:
    
        fields = ['name', ]
    
    class Meta:
       
        verbose_name = 'blog_user'
        
        verbose_name_plural = 'blog_users'
            
    def __str__(self):
    
        return self.name
from django.db import models
from authenticate.models import BlogUser

class Likes(models.Model):
    """
    Table for likes for posts
    """
    liked_at = models.DateTimeField(auto_now_add=True)
    post_id = models.ForeignKey(
        'Posts',
        models.CASCADE,
        related_name='likes'
    )
    user_id = models.ForeignKey(
        BlogUser,
        models.CASCADE,
        related_name='liked_posts'
    )
            
    class Meta:
        """
        Meta data for appropriate table descriptions
        """
        ordering = ['-liked_at']
        unique_together = ('user_id', 'post_id')
        verbose_name = 'liked_post'
        verbose_name_plural = 'liked_posts'
        
    def __str__(self):
        return f'{self.user_id} likes {self.post_id}'
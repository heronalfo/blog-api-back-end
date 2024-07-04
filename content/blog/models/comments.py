from django.db import models
from authenticate.models import BlogUser

class Comments(models.Model):
    """
    Comments related to user and post
    """
    content = models.CharField(
        blank=True,
        help_text='Content of comment for post',
        max_length=80,
    )
    commented_at = models.DateTimeField(auto_now_add=True)
    post_id = models.ForeignKey(
        'Posts',
        models.DO_NOTHING,
        related_name='comments'
    )
    user_id = models.ForeignKey(
        BlogUser,
        models.DO_NOTHING,
        related_name='comments'
    )
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta data for appropriate table descriptions
        """
        ordering = ['-commented_at']
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        
    def __str__(self):
        return self.content
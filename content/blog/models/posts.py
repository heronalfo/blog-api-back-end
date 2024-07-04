from django.db import models
from authenticate.models import BlogUser
from .tags import Tags

class Posts(models.Model):
    """
    Table for post
    """
    content = models.CharField(
        max_length=192,
        blank=True,
        help_text='Content for post'
    )
    user_id = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    posted_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(
        Tags,
        related_name='posts',
        blank=True
    )
    update_at = models.DateTimeField(auto_now=True)

    class Index:
        """
        Index for optimization of table
        """
        fields = ['content']

    class Meta:
        """
        Meta data for appropriate table descriptions
        """
        ordering = ['-posted_at']
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def quantity_of_likes(self):
        return self.likes.count()

    def __str__(self):
        """
        String formatting
        """
        return self.content
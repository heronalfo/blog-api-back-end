from django.db import models

class Tags(models.Model):
    """
    Post markings and better algorithm stability
    """
    tag = models.CharField(max_length=100, unique=True)
    
    class Meta:
        """
        Meta data for appropriate table descriptions
        """
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
    
    def __str__(self):
        return self.tag
from rest_framework import serializers
from blog.models.comments import Comments

class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
    
        model = Comments
        fields = ['content', 'user_id', 'commented_at', 'update_at', 'post_id']
        
        read_only_fields = ['user_id', 'commented_at', 'update_at', 'post_id']
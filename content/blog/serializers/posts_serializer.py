from rest_framework import serializers
from blog.models.posts import Posts

class PostsSerializer(serializers.ModelSerializer):

    class Meta:
    
        model = Posts
        fields = ['content', 'user_id', 'posted_at', 'update_at', 'tags']
        
        read_only_fields = ['user_id', 'posted_at', 'update_at', 'tags']
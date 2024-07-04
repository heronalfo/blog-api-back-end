from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_xml.renderers import XMLRenderer
from blog.models.posts import Posts
from blog.serializers
posts_serializer import PostsSerializer

class PostsViewSet(ModelViewSet):

    queryset = Posts.objects.all()    
    serializer_class = PostsSerializer    
    renderer_classes = [JSONRenderer, XMLRenderer] 
    
    parser_classes = [JSONParser, XMLParser]    
    http_method_names = ['get', 'post', 'delete', 'patch', 'options', 'head']
    
    def perform_create(self, serializer):        
        serializer.save(user_id=self.request.user)
        
    def get_object(self):    
        obj = get_object_or_404(        
          self.get_queryset(),
          pk=self.kwargs.get('pk')
          
        )
        
        self.check_object_permissions(self.request, obj)
        
        return obj
        
    def get_permissions(self):    
        if self.action == 'create':        
            return [IsAuthenticated()]
            
        if self.action in ['destroy', 'update']:        
            return [IsOwner()]
        
        return super().get_permissions()
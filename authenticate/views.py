from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .serializers import CreateUserSerializer

class AuthenticationCreateUser(APIView):

    serializer_class = CreateUserSerializer

    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]    
    def post(self, request):
    
        data = request.data

        serializer = self.get_serializer(data=data)
        
        if serializer.is_valid(raise_exception=True):
        
            User.objects.create_user(username=data.get('username'), password=data.get('password'))
            
            return Response({'detail': 'Create user {data.get("username")}'}, status=STATUS.HTTP_201_CREATED)
        
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
        
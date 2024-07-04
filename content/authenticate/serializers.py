from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import status

class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
    
        model = User
        fields = [ 'username', 'password' ]
    
    def validate(self, attrs):
    
        _validate = super().validate(attrs)
                
        if User.objects.all().filter(username=attrs.get('username')).exists():
        
            raise serializers.ValidationError({'detail': 'The username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        if len(attrs.get('password')) < 8:
        
            raise serializers.ValidationError({'detail': 'The PASSWORD must have 8 or more chadacters'}, status=status.HTTP_400_BAD_REQUEST)
        
        
                                   
        return _validate
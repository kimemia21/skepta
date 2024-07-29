from rest_framework.serializers import ModelSerializer
from .models import Post,Author,Comment
from django.contrib.auth.models import User




class PostSerializer(ModelSerializer):
    class Meta:
        model =Post
        fields ="__all__"
        
class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
        
class AuthorSerializer(ModelSerializer):
    class Meta:
        
        model =Author
        fields ="__all__"

class CommentsSerializer(ModelSerializer):
    class Meta:
        model =Comment
        fields ="__all__"
        
                    
        
        
        
from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Author,Post,Comment
from .serializer import PostSerializer,UserSerializer,CommentsSerializer,AuthorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["POST"])
def login(request):
    data = request.data
    username = data.get("username")
    password = data.get("password")

    # Check if username and password are provided
    if not username or not password:
        return Response({"message": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    # Authenticate the user
    user = authenticate(username=username, password=password)
    if user is not None:
        return Response({"message": "User is valid"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
    
@api_view(["POST"])
def signUp(request):
    data =request.data
    serializer =UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        user =get_object_or_404(User,username=data["username"])
        user.set_password(data["password"])
        user.save()
        loginserializer =UserSerializer(user)
        return Response(loginserializer.data,status=status.HTTP_200_OK)
    else:
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)    



@api_view(["GET"])
def getPosts(request):
    if request.method =="GET":
        obj =Post.objects.all()
        seriailizer =PostSerializer(obj,many=True)
        return Response(seriailizer.data,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)









# Create your views here.

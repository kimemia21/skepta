from django.urls import path
from .views import *


urlpatterns = [
    path("login",view=login),
    path("post",view=getPosts),
    path("signup",view=signUp),
    path("post/<int:pk>",view=post),
    path("comment/<int:pk>",view=comment),
    path("author/<int:pk>",view=author),
    path("addpost",view=addPost),
    path("addComment",view=addComment),
    
]

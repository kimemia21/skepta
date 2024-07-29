from django.urls import path
from .views import getPosts,login,signUp


urlpatterns = [
    path("login",view=login),
    path("post",view=getPosts),
    path("signup",view=signUp)
]

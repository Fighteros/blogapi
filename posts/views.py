from django.contrib.auth import get_user_model
from rest_condition import And, Or
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny

# Create your views here.
from posts.models import Post
from posts.serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadonly, IsSafeMethod, IsPostMethod


class PostDetial(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadonly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        Or(
            And(IsPostMethod, IsAdminUser),
            And(IsSafeMethod, AllowAny),
        )
    ]


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

from rest_framework import generics, permissions

# Create your views here.
from posts.models import Post
from posts.serializers import PostSerializer


class PostDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

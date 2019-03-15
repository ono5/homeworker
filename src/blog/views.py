from rest_framework import generics, permissions

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer


class BlogList(generics.ListCreateAPIView):
    # View-level permissions
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

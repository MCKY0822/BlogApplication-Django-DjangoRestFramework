from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Blog
from .serializers import BlogSerializer


class BlogListCreateView(generics.ListCreateAPIView):  # List and Create Blog Posts
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Set the author to the currently logged-in user


class BlogRetrieveDeleteView(generics.RetrieveDestroyAPIView):  # Retrieve and Delete Blog Post
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

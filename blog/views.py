from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Blog
from .serializers import BlogSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


class BlogListView(generics.ListAPIView): # List blog posts
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BlogCreateView(generics.CreateAPIView): # Create a new blog post
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Set the author to the currently logged-in user


class BlogRetrieveDeleteView(generics.RetrieveDestroyAPIView):  # Retrieve and Delete Blog Post
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'


@login_required
def home_view(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the home page (or any other page)
        else:
            # If login fails, display an error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    
    return render(request, 'login.html')
from django.shortcuts import render, redirect
from rest_framework import generics, permissions
from .models import Blog
from .serializers import BlogSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework.pagination import PageNumberPagination

class BlogPagination(PageNumberPagination): # for optimization
    page_size = 5  # set the number of blog posts per page


class BlogListView(generics.ListAPIView): # list blog posts
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = BlogPagination  # enable pagination for optimization


class BlogCreateView(generics.CreateAPIView): # create a new blog post
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # set the author to the currently logged-in user


class BlogDeleteView(generics.RetrieveDestroyAPIView):  # retrieve and Delete Blog Post
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'id'


@login_required
def home_view(request):
    blogs = Blog.objects.all()  # retrieve all blog posts / optional requirement
    return render(request, 'home.html', {'blogs': blogs})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # log the user in
            return redirect('home')  # redirect to the home page
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'}) # display an error message
    
    return render(request, 'login.html')
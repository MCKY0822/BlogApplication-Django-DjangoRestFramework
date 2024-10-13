from django.urls import path
from .views import BlogListView, BlogCreateView, BlogRetrieveDeleteView, login_view, home_view

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog-list'),  # URL for listing blog posts
    path('blogs/create/', BlogCreateView.as_view(), name='blog-create'),  # URL for creating a blog post
    path('blogs/<int:id>/', BlogRetrieveDeleteView.as_view(), name='blog-retrieve-delete'),  # URL for retrieving and deleting a blog post
    path('login/', login_view, name='login'),  # URL for login
    path('home/', home_view, name='home'),  # URL for home view
]
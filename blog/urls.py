from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDeleteView, login_view, home_view

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blogs/create/', BlogCreateView.as_view(), name='create_blog'),
    path('blogs/<int:id>/', BlogDeleteView.as_view(), name='delete_blog'),
]

from django.urls import path
from . views import BlogListCreateView, BlogDeleteView

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<int:id>/', BlogDeleteView.as_view(), name='blog-delete'),
]

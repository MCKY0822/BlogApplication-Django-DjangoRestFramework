from django.urls import path
from .views import BlogListCreateView, BlogRetrieveDeleteView

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<int:id>/', BlogRetrieveDeleteView.as_view(), name='blog-retrieve-delete'),
]

from django.urls import path
from .views import BlogListCreateView, BlogRetrieveDeleteView, login_view, home_view 

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<int:id>/', BlogRetrieveDeleteView.as_view(), name='blog-retrieve-delete'),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
]

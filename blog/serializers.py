from rest_framework import serializers
from . models import Blog


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)


    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'author']
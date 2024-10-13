from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # to display in the list view
    list_filter = ('author', 'created_at') # to filter by in the admin panel
    search_fields = ('title', 'content', 'author__username') # to search in the admin panel


admin.site.register(Blog, BlogAdmin) # register the Blog model with the custom admin class
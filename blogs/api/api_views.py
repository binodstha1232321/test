from rest_framework.response import Response
from event.blogs.api import serializers
from rest_framework import viewsets, permissions
from event.blogs.models import Blog

class BlogView(viewsets.ViewSet):
    serializer_class = serializers.BlogSerializer
    queryset= Blog.objects.all()
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]

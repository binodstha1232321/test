from rest_framework.response import Response
from event.blogs.api import serializers
from rest_framework import viewsets
# from e
from event.blogs.models import Blog

class BlogView(viewsets.ViewSet):
    # serializer_class = serializers.BlogSerializer
    # model_class_blog = Blog.objects.all()
    def list(self,request):
        model_class_blog = Blog.objects.all()
        serializer_class = BlogSerializer(model_class_blog,many=True)
        return Response(serializer_class.data)
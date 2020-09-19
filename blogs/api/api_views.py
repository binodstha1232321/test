from rest_framework.response import Response
from event.blogs.api.serializers import UserSerializer
from event.blogs.api import serializers
from rest_framework import viewsets, permissions
from event.blogs.models import Blog
from django.contrib.auth.models import User


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
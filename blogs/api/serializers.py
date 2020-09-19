from rest_framework import serializers
from event.blogs.models import Blog
from django.contrib.auth.models import User

# class BlogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Blog
#         fields = '__all__'
#         extra_kwargs = {
#             'title':{
#                 'read_only':True,
#                 # 'style':{'input_type':'password'}
#             }
#         }


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
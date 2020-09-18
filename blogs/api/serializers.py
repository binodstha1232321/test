from rest_framework import serializers
from event.blogs.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        extra_kwargs = {
            'title':{
                'read_only':True,
                # 'style':{'input_type':'password'}
            }
        }
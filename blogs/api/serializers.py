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
    
    def create(self, validated_data):
        """
        create and return a new 'Snippet' instance, given the validated_data 
        """
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.content = validated_data.get('content', instance.content)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.featured = validated_data.get('featured', instance.featured)
        instance.block = validated_data.get('block', instance.block)
        instance.date_added = validated_data.get('date_added', instance.date_added)
        instance.date_edited = validated_data.get('date_edited', instance.date_edited)
        instance.save()
        return instance
from rest_framework import serializers
from event.core.models import FAQ, Contact


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class Contact(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

from core.api.serializers import FAQSerializer, ContactSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from core.models import FAQ, Contact

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.object.all()
    seriralizer_class = FAQSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
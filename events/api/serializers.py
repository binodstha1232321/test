from rest_framework import serializers
from event.events.models import Category,Person,Organiser,Speaker,Schedule,Program,Event,File


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class OrganiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organiser
        fields = '__all__'

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class ProgramSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class EventSerializer(serializers.Serializer):
    class Meta:
        model = Event
        fields = '__all__'

class FileSerialzer(serializers.Serializer):
    class Meta:
        model = File
        fields = '__all__'




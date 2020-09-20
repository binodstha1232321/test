
from rest_framework import routers

from blogs.views import BlogViewSet
from core.views import ContactViewSet
from events.api.api_views import EventViewSet,FileViewSet,SpeakerViewSet,ScheduleViewSet,OrganiserViewSet,CategoryViewSet,PersonViewSet,ProgramViewSet


from blogs.api.api_views import UserViewSet
router = routers.DefaultRouter()

router.register('users', UserViewSet)
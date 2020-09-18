from rest_framework.routers import DefaultRouter
from rest_framework import routers

# from event.core import
from event.blogs.api.api_views import BlogView

router = routers.DefaultRouter()
router.register('blog',BlogView,basename="blog")
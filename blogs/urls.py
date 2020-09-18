from django.urls import path,include
from . import views
from .api.api_views import BlogView
from rest_framework import routers

router = routers.DefaultRouter()

router.register('blog-api',BlogView.as_view,basename="blog-api")

urlpatterns = [
    # path('',views.index,name="index"),
    router.urls
]

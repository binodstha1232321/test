from django.urls import path
from . import views
from .views import BlogAPIView,BlogDetail
urlpatterns = [
    path('',views.index,name = "index"),
    path('get-data/',BlogAPIView.as_view()),
    path('get-data/<int:pk>/',BlogDetail.as_view())
]
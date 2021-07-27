from rest_framework import routers
from django.urls import path, include 

from . import views

router = routers.DefaultRouter() #already handled in api.urls
router.register(r'', views.CategoryViewSet)

urlpatterns = [
        path('', include(router.urls))
        ]

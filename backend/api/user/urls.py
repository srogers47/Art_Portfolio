from rest_framework import routers
from django.urls import path, include 

from . import views 

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [ 
        path('login/', views.signin, name='signin'),
        #<> notation required to retrieve id param of signout in views. 
        path('logout/<int:id>/', views.signout, name='signout'), 
        path('', include(router.urls)) 
        ]

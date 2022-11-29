from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'trip', TripViewSet)


urlpatterns = [
    path('', include(router.urls))
]
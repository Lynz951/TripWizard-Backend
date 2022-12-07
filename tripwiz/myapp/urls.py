from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'trip', TripViewSet)
router.register(r'customuser', CustomUserViewSet)
router.register(r'plantype', PlanTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("plan/<int:trip_id>/", Trip_PlanAPIView.as_view(), name="TripPlanLookup")
]
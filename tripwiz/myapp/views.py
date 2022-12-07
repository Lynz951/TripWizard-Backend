from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response

# Create your views here.

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class TripViewSet(ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class PlanTypeViewSet(ModelViewSet):
    queryset = PlanType.objects.all()
    serializer_class = PlanTypeSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class Trip_PlanAPIView(APIView):

    def get_object(self, trip_id):
        try:
            return Plan.objects.get(trip_id=trip_id)
        except Plan.DoesNotExist:
            raise Http404

    def get(self, request, trip_id=None, format=None):
        if trip_id:
            data = self.get_object(trip_id)
            serializer = PlanSerializer(data)
        else:
            data = Plan.objects.all()
            serializer = PlanSerializer(data, many=True)
        
        return Response(serializer.data)
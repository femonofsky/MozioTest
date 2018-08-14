from django.shortcuts import render
from django.contrib.gis.geos import Point
# Create your views here.
from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from polygons.models import Provider, ServiceArea
from polygons.serializers import ProviderSerializer, ServiceAreaSerializer
from rest_framework.decorators import action


# using django rest framework for the API


class ProviderView(ListCreateAPIView):
    """
    Endpoint for creating new providers and fetching providers list. \n
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderDetails(RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaView(ListCreateAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class ServiceAreaDetails(RetrieveUpdateDestroyAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class ServiceAreaAPI(APIView):
    def get(self, request, *args, **kwargs):
        params = request.query_params
        lat = params.get('lat', None)
        lng = params.get('lng', None)
        if lat and lng:
            try:
                lng = float(lng)
                lat = float(lat)
                pnt = Point(lng, lat)
            except (TypeError, ValueError):
                raise APIException('lat or lng format is invalid')
            service_areas = ServiceArea.objects.filter(polygon__intersects=pnt)
            serializer = ServiceAreaSerializer(service_areas, many=True)
            return Response(serializer.data)
        else:
            raise APIException('Both lat and lng parameters are required')


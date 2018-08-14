from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from polygons.models import Provider
from polygons.serializers import ProviderSerializer

# using django rest framework for the API


class ProviderView(ListCreateAPIView):
    """
    Endpoint for creating new providers and fetching providers list. \n
    Currency argument must be a 3-letter or a 3-digit code
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderDetail(RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
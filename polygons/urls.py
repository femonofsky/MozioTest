from django.urls import path
from django.conf.urls import url

from polygons import views

urlpatterns = [
    path('v1/providers/', views.ProviderView.as_view(), name='providers'),
    path('v1/providers/<uuid:pk>/', views.ProviderDetail.as_view(),
        name='providers_details'),
]


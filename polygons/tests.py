from rest_framework import status
from rest_framework.test import APITestCase

from .models import *


class ProviderTest(APITestCase):
    def setUp(self):
        self.data = {'name': 'Akinnurun Oluwafemi Samuel', 'email': 'test@test.com', 'language': 'en',
                     'currency': 'USD', 'phone_number': '+234905556903'}
        self.data_test = {'name': 'Akinnurun Oluwafemi Samuel', 'email': 'go@test.com', 'language': 'en',
                     'currency': 'USD', 'phone_number': '+234905556903'}
        self.provider = Provider.objects.create(**self.data)
        self.data.update({'email': 'femmy4lov@gmail.com'})

    def test_can_create_provider(self):
        response = self.client.post('/service_areas/v1/providers/', self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_read_provider_list(self):
        response = self.client.get('/service_areas/v1/providers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_provider_detail(self):
        response = self.client.get('/service_areas/v1/providers/' + str(self.provider.id) + "/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_user(self):
        response = self.client.put('/service_areas/v1/providers/' + str(self.provider.id) + "/", self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Provider.objects.get(pk=self.provider.id).email, 'femmy4lov@gmail.com')

    def test_can_delete_user(self):
        response = self.client.delete('/service_areas/v1/providers/' + str(self.provider.id) + "/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateServiceAreaTest(APITestCase):
    def setUp(self):
        self.provider_data = {'name': 'Akinnurun Oluwafemi Samuel', 'email': 'test@gmail.com', 'language': 'en',
                     'currency': 'USD', 'phone_number': '+234905556903'}
        self.provider = Provider.objects.create(**self.provider_data)
        self.service_area_data = {'name': 'Test area', 'price': '10.5', 'provider_id': self.provider.id,
                          'polygon':'POLYGON(( 10 10, 10 20, 20 20, 20 15, 10 10))'}

    def test_can_create_area(self):
        response = self.client.post('/service_areas/v1/service_areas/', self.service_area_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadServiceAreaTest(APITestCase):
    def setUp(self):
        self.provider_data = {'name': 'Akinnurun Oluwafemi Samuel', 'email': 'test@gmail.com', 'language': 'en',
                              'currency': 'USD', 'phone_number': '+234905556903'}

        self.provider = Provider.objects.create(**self.provider_data)
        self.service_area_data = {'name': 'Test area', 'price': '10.5', 'provider_id': self.provider.id,
                          'polygon': 'POLYGON(( 10 10, 10 20, 20 20, 20 15, 10 10))'}
        self.service_area = ServiceArea.objects.create(provider=self.provider, **self.service_area_data)

    def test_can_read_service_area_list(self):
        response = self.client.get('/service_areas/v1/service_areas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_service_area_detail(self):
        response = self.client.get('/service_areas/v1/service_areas/' + str(self.service_area.id) + "/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateDestroyServiceAreaTest(APITestCase):
    def setUp(self):
        self.provider_data = {'name': 'Akinnurun Oluwafemi Samuel', 'email': 'test@gmail.com', 'language': 'en',
                              'currency': 'USD', 'phone_number': '+234905556903'}

        self.provider = Provider.objects.create(**self.provider_data)
        self.service_area_data = {'name': 'Test area', 'price': '40.25',
                          'polygon': 'POLYGON(( 10 10, 10 20, 20 20, 20 15, 10 10))'}
        self.service_area = ServiceArea.objects.create(provider=self.provider, **self.service_area_data)

        self.service_area_data.update({'price': '50'})


    def test_can_update_area(self):
        response = self.client.put('/service_areas/v1/service_areas/' + str(self.service_area.id) + "/",
                                   self.service_area_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ServiceArea.objects.get(pk=self.service_area.id).price, '50')

    def test_can_find_correct_query(self):
        response = self.client.get(
            '/service_areas/v1/get_areas/?lat={}&lng={}'.format("15.0", "10.0"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['features']), 1)

    def test_can_delete_service_area(self):
        response = self.client.delete('/service_areas/v1/service_areas/' + str(self.service_area.id) + "/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



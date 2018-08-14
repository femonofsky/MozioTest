from django.contrib.gis.db import models 
import uuid
from django.conf.global_settings import LANGUAGES


# Create your models here.
class Provider (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Provider Name", max_length=255)
    email = models.EmailField("Provider Email", unique=True, max_length=255)
    phone_number = models.CharField("Provider Phone Number", max_length=255)
    language = models.CharField("Provider Language", max_length=10, choices=LANGUAGES, default='en')
    currency = models.CharField("Provider Currency", max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '%s - %s - %s - %s - %s' % (self.name.title(), self.email.title(), self.phone_number.title(),
                                      self.language.title(), self.currency.title())


class ServiceArea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE, related_name='service_areas')
    name = models.CharField("Name", max_length=100)
    price = models.DecimalField("Price", max_digits=100, decimal_places=2)
    polygon = models.PolygonField("Polygon", geography=True)

    def __str__(self):
        return '%s - %s ' % (self.provider.name.title(), self.name.title())

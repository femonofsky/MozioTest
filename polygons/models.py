from django.db import models
import uuid


# Create your models here.
class Provider (models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Provider Name", max_length=255)
    email = models.EmailField("Provider Email", max_length=255)
    phone_number = models.CharField("Provider Phone Number", max_length=255)
    language = models.CharField("Provider Language", max_length=255)
    currency = models.CharField("Provider Currency", max_length=100)

    def __str__(self):
        return '%s - %s - %s - %s - %s' % (self.name.title(), self.email.title(), self.phone_number.title(),
                                      self.language.title(), self.currency.title())
from django.db import models

class Address(models.Model):
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=128)
    number = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.country} - {self.city} - {self.street} - {self.number}'

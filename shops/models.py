from django.db import models

class Shop(models.Model):
    address = models.ForeignKey('address.Address', on_delete=models.CASCADE)

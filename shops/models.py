from django.db import models

class Shop(models.Model):
    branch = models.CharField(max_length=256, unique=True)
    address = models.ForeignKey('address.Address', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.branch} --- {self.address}'

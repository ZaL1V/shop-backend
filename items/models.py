from django.db import models
from django.utils.translation import gettext as _


class Items(models.Model):
    class SexChoises(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        UNISEX = 'U', _('Unisex')

    article =  models.CharField(unique=True, max_length=128)
    title = models.CharField(max_length=256)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    sex = models.CharField(max_length=8, choices=SexChoises.choices, default=SexChoises.UNISEX)
    size = models.JSONField()
    shop = models.ForeignKey('shops.Shop', on_delete=models.CASCADE)
    image = models.JSONField()


    def __str__(self):
        return self.article

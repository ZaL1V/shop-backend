from django.contrib import admin
from .models import Address

@admin.register(Address)
class AddressAdmins(admin.ModelAdmin):
    list_display = (
        'country',
        'city',
        'street',
        'number'
    )

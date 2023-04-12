from django.contrib import admin
from .models import Items

@admin.register(Items)
class ItemAdmins(admin.ModelAdmin):
    list_display = (
        'article',
        'title',
        'category',
        'price',
        'discount_price',
        'sex',
        'size',
        'shop',
        'image',
    )

    search_fields = ('article', 'title')

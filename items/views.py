from rest_framework import viewsets
from .models import Items
from .serializers import ItemsSerializer
from .pagination import DefaultPagination


class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    pagination_class = DefaultPagination

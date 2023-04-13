from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


app_name = 'items'

router = DefaultRouter()
router.register('items', views.ItemsViewSet, 'items')

urlpatterns = [
    path('', include(router.urls))
]

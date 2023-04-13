from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


app_name = 'address'

router = DefaultRouter()
router.register('address', views.AddressViewSet, 'address')

urlpatterns = [
    path('', include(router.urls))
]

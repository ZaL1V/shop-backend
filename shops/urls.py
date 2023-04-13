from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


app_name = 'shop'

router = DefaultRouter()
router.register('shop', views.ShopViewSet, 'shop')

urlpatterns = [
    path('', include(router.urls))
]

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


app_name = 'category'

router = DefaultRouter()
router.register('items', views.CategoryViewSet, 'category')

urlpatterns = [
    path('', include(router.urls))
]

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs',
    ),
    path('api/' , include('items.urls')),
    path('api/' , include('category.urls')),
    path('api/' , include('address.urls')),
    path('api/' , include('shops.urls')),
    path('api/' , include('users.urls')),
    path('', admin.site.urls),
]

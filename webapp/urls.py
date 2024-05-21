from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from website import views as website_views
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda req: redirect('home')),
    path('api/', include('api.urls')),
    path('home/', website_views.HomeView.as_view(), name='home'),
    path('product/', website_views.ProductsView.as_view(), name='product'),
    path('product/search', website_views.ProductSearchView.as_view(), name='search_product'),
]

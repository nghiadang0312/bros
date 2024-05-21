from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('product/', views.ProductList.as_view()),
    path('product/<str:pk>/', views.ProductDetail.as_view()),
    path('warehouse/', views.WarehouseList.as_view()),
    path('warehouse/<str:pk>/', views.WarehouseDetail.as_view()),
    path('customer/', views.CustomerList.as_view()),
    path('customer/<str:pk>/', views.CustomerDetail.as_view()),
]

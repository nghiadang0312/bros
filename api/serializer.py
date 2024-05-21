from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from django.contrib.auth import get_user_model
from website.models import Products, Warehouse, Customers, Invoice, InvoiceItem

User = get_user_model()


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = ("idProduct", "nameProduct", "descriptionProduct", "idWarehouse", "quantityProduct", "expirationDate")


class WarehouseSerializer(ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ("idWarehouse", "nameWarehouse", "locationWarehouse")


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customers
        fields = ("idCustomer", "nameCustomer", "emailCustomer", "phoneCustomer", "addressCustomer")
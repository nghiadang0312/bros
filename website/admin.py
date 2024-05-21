from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from website.models import Account, Products, Warehouse, Customers, Invoice, InvoiceItem
import csv
from django.http import HttpResponse

User = get_user_model()


@admin.register(User)
class ManagerAccount(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Account Info'), {
            'fields': ('idAcc',
                       'nameAcc',
                       'email')
        }),
        (_('Permission'), {
            'fields': ('is_staff',
                       'is_active',
                       'is_superuser',
                       'groups',
                       'user_permissions')
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username',
                       'idAcc',
                       'email',
                       'password1',
                       'password2'),
        }),
    )
    list_display = ('idAcc', 'nameAcc', 'email')
    search_fields = ('idAcc', 'nameAcc', 'email')
    ordering = ('idAcc',)
    filter_horizontal = ('groups', 'user_permissions',)
    list_per_page = 30


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Products._meta.fields]
    list_filter = list_display
    search_fields = ["idProduct", "nameProduct"]


class WarehouseAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Warehouse._meta.fields]
    list_filter = list_display
    search_fields = ["idWarehouse", "nameWarehouse"]


class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Customers._meta.fields]
    list_filter = list_display
    search_fields = ["idCustomers", "nameCustomers", "phoneCustomer"]


class InvoiceAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Invoice._meta.fields]
    list_filter = list_display
    search_fields = ["idInvoice"]


class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in InvoiceItem._meta.fields]
    list_filter = list_display
    search_fields = ["idInvoiceItem"]


admin.site.unregister(Group)
admin.site.register(Products, ProductAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Customers, CustomerAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)

admin.site.site_url = '/home'
admin.site.site_header = 'TRANG QUẢN TRỊ HỆ THỐNG'
admin.site.site_title = 'Trang quản trị hệ thống'
admin.site.index_title = 'Quản trị'

import datetime

import django
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Account(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    idAcc = models.CharField(_('Mã số tài khoản'),
                             primary_key=True,
                             blank=False,
                             max_length=10,
                             error_messages={
                                 'unique': _('Mã số đã được sử dụng')
                             })
    username = models.CharField(
        _('username'),
        max_length=40,
        unique=True,
        help_text=_('Tối đa 40 ký tự. Chỉ gồm chữ cái, số và @/./+/-/_'),
        validators=[username_validator],
        error_messages={
            'unique': _("Tài khoản này đã được sử dụng."),
        },
    )
    email = models.EmailField(_('Địa chỉ mail'), unique=True,
                              error_messages={
                                  'unique': _("Mail đã được sử dụng."),
                              })
    is_staff = models.BooleanField(
        _('Là nhân viên'),
        default=False,
        help_text=_('Chỉ định liệu người dùng có thể đăng nhập vào trang quản trị này hay không.'),
    )
    is_active = models.BooleanField(
        _('Được kích hoạt'),
        default=True,
        help_text=_(
            'Chỉ định xem người dùng này có nên được coi là đang hoạt động hay không.'
            'Bỏ chọn mục này thay vì xóa tài khoản.'
        ),
    )
    first_name = None
    last_name = None
    nameAcc = models.CharField(_('Tên'), max_length=100, default='')
    REQUIRED_FIELDS = ['idAcc', 'email']

    def __str__(self):
        return self.idAcc


class Warehouse(models.Model):
    idWarehouse = models.CharField(_('Mã kho'), primary_key=True, max_length=30)
    nameWarehouse = models.CharField(_('Tên kho'), max_length=255)
    locationWarehouse = models.TextField(_('Vị trí kho'))

    def __str__(self):
        return self.nameWarehouse


class Products(models.Model):
    idProduct = models.CharField(_('Mã sản phẩm'), primary_key=True, max_length=30)
    idWarehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    nameProduct = models.CharField(_('Tên sản phẩm'), max_length=255)
    descriptionProduct = models.TextField(_('Mô tả'))
    quantityProduct = models.IntegerField(_('Số lượng sản phẩm hiện có'), default=0)
    expirationDate = models.DateField(_('Hạn sử dụng'), null=False, blank=False)

    def __str__(self):
        return self.nameProduct


class Customers(models.Model):
    idCustomer = models.AutoField(_('Mã khách hàng'), primary_key=True)
    nameCustomer = models.CharField(_('Tên khách hàng'), max_length=255)
    emailCustomer = models.EmailField(_('email khách hàng'), null=True, blank=True)
    phoneCustomer = models.CharField(_('Số điện thoại'), max_length=10, null=False, blank=False, unique=True)
    addressCustomer = models.TextField(_("Địa chỉ khách hàng"), null=False, blank=False)

    def __str__(self):
        return self.nameCustomer


class Invoice(models.Model):
    idInvoice = models.CharField(_('Mã hóa đơn'), primary_key=True, max_length=30)
    idCustomer = models.OneToOneField(Customers, on_delete=models.CASCADE)
    invoiceDate = models.DateField(_('Ngày xuất hóa đơn'), default=django.utils.timezone.now)
    totalPrice = models.DecimalField(_('Tổng số tiền'), null=False, blank=False, max_digits=20, decimal_places=6)


class InvoiceItem(models.Model):
    idInvoiceItem = models.AutoField(_('Mã chi tiết hóa đơn'), primary_key=True)
    idInvoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    idProduct = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(_("Số lượng sản phẩm trong chi tiết hóa đơn"))
    unitPrice = models.DecimalField(_('Giá mỗi sản phẩm'), null=False, blank=False, max_digits=20, decimal_places=6)
    totalPrice = models.DecimalField(_('Tổng giá sản phẩm'), null=False, blank=False, max_digits=20, decimal_places=6)

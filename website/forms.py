from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.admin import UserCreationForm
from django.contrib.auth.forms import UsernameField
from django.utils.translation import gettext_lazy as _

from website.models import Warehouse, Products

User = get_user_model()


class UpdateInfoFormClass(forms.ModelForm):
    class Meta:
        model = User
        fields = ('nameAcc',)


class RegisterForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _('Mật khẩu không khớp'),
    }
    password1 = forms.CharField(
        label=_("Mật khẩu"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=_("Mật khẩu phải có ít nhất 8 ký tự và không bắt đầu bằng số"),
    )
    password2 = forms.CharField(
        label=_("Nhập lại mật khẩu"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ('idAcc',
                  'username',
                  'nameAcc',
                  'email',
                  'password1',
                  'password2',)
        widgets = {

        }

    field_classes = {'username': UsernameField}


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('idProduct', 'nameProduct', 'idWarehouse',
                  'descriptionProduct', 'quantityProduct', 'expirationDate')
        labels = {
            "idProduct": "Mã sản phẩm",
            "nameProduct": "Tên sản phẩm",
            "idWarehouse": "Kho",
            "descriptionProduct": "Mô tả",
            "quantityProduct": "Số lượng",
            "expirationDate": "Hạn sử dụng"
        }

    def __init__(self, *args, **kwargs):
        super(UpdateProductForm, self).__init__(*args, **kwargs)
        # self.fields['idProduct'].readOnly = True



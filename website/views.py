from django.contrib.auth import login, get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import FormView

from website.forms import RegisterForm, UpdateProductForm
from website.models import Products, Warehouse

User = get_user_model()


# Create your views here.

class RegisterViewClass(FormView):
    template_name = 'user/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create(
            username=data['username'],
            email=data['email'],
            password=data['password1'],
            idAcc=data['idAcc'],
            nameAcc=data['nameAcc'],
        )
        new_user.set_password(data['password1'])
        new_user.save()
        login(self.request, new_user)
        url = f"{reverse('info')}"
        return redirect(url)


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {'nav': 'home'})


class ProductsView(View):
    def get(self, request):
        return render(request, 'product/product.html', {'nav': 'product'})


class ProductSearchView(View):
    def get(self, request):
        product = Products.objects.all()
        editProductsForm = UpdateProductForm
        return render(request, 'product/search.html', {'nav': 'product',
                                                       "data": product,
                                                       "editProductsForm": editProductsForm})

    def post(self, request):
        data = request.POST
        warehouse = Warehouse.objects.get(idWarehouse=data.get('idWarehouse'))
        if data.get('checkbox_delete') == "on":
            pro = Products.objects.get(idProduct=data.get('idProduct'))
            pro.delete()
        else:
            try:
                pro = Products.objects.get(idProduct=data.get('idProduct'))
                pro.idWarehouse = warehouse
                pro.nameProduct = data.get('nameProduct')
                pro.descriptionProduct = data.get('descriptionProduct')
                pro.quantityProduct = data.get('quantityProduct')
                pro.expirationDate = data.get('expirationDate')
                pro.save()
            except Products.DoesNotExist:
                pro = Products.objects.create(
                    idProduct=data.get('idProduct'),
                    idWarehouse=warehouse,
                    nameProduct=data.get('nameProduct'),
                    descriptionProduct=data.get('descriptionProduct'),
                    quantityProduct=data.get('quantityProduct'),
                    expirationDate=data.get('expirationDate'),
                )

        product = Products.objects.all()
        editProductsForm = UpdateProductForm
        return render(request, 'product/search.html', {'nav': 'product',
                                                       "data": product,
                                                       "editProductsForm": editProductsForm})
from django.forms import ModelForm
from django import forms
from .models import Product, Supplier, Warehouse, Order, Stock

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"

class WarehouseForm(ModelForm):
    class Meta:
        model = Warehouse
        fields = "__all__"

class OrderForm(ModelForm):
    order_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Order
        fields = "__all__"

class StockForm(ModelForm):
    expire_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Stock
        fields = "__all__"

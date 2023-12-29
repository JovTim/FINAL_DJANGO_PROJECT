from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Product, Supplier, Warehouse, Order, Stock
from .forms import ProductForm, SupplierForm, WarehouseForm, OrderForm, StockForm

from django.urls import reverse_lazy

class HomePageView(ListView):
    model = Product
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProductList(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'product.html'
    paginate_by = 6

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_add.html'
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView): #ERROR
    model = Product
    form_class = ProductForm
    template_name = 'product_edit.html'
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView): #ERROR
    model = Product
    template_name = 'product_del.html'
    success_url = reverse_lazy('product-list')

class SupplierList(ListView):
    model = Supplier
    context_object_name = 'supplier-list'
    template_name = 'supplier.html'
    paginate_by = 6

class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplier_add.html'
    success_url = reverse_lazy('supplier-list')

class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplier_edit.html'
    success_url = reverse_lazy('supplier-list')

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'supplier_del.html'
    success_url = reverse_lazy('supplier-list')

class WarehouseList(ListView):
    model = Warehouse
    context_object_name = 'warehouse-list'
    template_name = 'warehouse.html'
    paginate_by = 6

class WarehouseCreateView(CreateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name = 'warehouse_add.html'
    success_url = reverse_lazy('warehouse-list')

class WarehouseUpdateView(UpdateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name = 'warehouse_edit.html'
    success_url = reverse_lazy('warehouse-list')

class WarehouseDeleteView(DeleteView):
    model = Warehouse
    template_name = 'warehouse_del.html'
    success_url = reverse_lazy('warehouse-list')

class OrderList(ListView):
    model = Order
    context_object_name = 'order-list'
    template_name = 'order.html'
    paginate_by = 6

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_add.html'
    success_url = reverse_lazy('order-list')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_edit.html'
    success_url = reverse_lazy('order-list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_del.html'
    success_url = reverse_lazy('order-list')



class StockList(ListView):
    model = Stock
    context_object_name = 'stock-list'
    template_name = 'stock.html'
    paginate_by = 6

class StockCreateView(CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'stock_add.html'
    success_url = reverse_lazy('stock-list')

class StockUpdateView(UpdateView):
    model = Stock
    form_class = StockForm
    template_name = 'stock_edit.html'
    success_url = reverse_lazy('stock-list')

class StockDeleteView(DeleteView):
    model = Stock
    template_name = 'stock_del.html'
    success_url = reverse_lazy('stock-list')
# Create your views here.

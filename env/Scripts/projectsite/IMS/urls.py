"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    
    path('product_list', ProductList.as_view(), name='product-list'),
    path('product_list/add', ProductCreateView.as_view(), name='product-add'),
    path('product_list/<pk>', ProductUpdateView.as_view(), name='product-update'),
    path('product_list/<pk>/delete', ProductDeleteView.as_view(), name='product-delete'),

    path('supplier_list', SupplierList.as_view(), name='supplier-list'),
    path('supplier_list/add', SupplierCreateView.as_view(), name='supplier-add'),
    path('supplier_list/<pk>', SupplierUpdateView.as_view(), name='supplier-update'),
    path('supplier_list/<pk>/delete', SupplierDeleteView.as_view(), name='supplier-delete'),

    path('warehouse_list', WarehouseList.as_view(), name='warehouse-list'),
    path('warehouse_list/add', WarehouseCreateView.as_view(), name='warehouse-add'),
    path('warehouse_list/<pk>', WarehouseUpdateView.as_view(), name='warehouse-update'),
    path('warehouse_list/<pk>/delete', WarehouseDeleteView.as_view(), name='warehouse-del'),

    path('order_list', OrderList.as_view(), name='order-list'),
    path('order_list/add', OrderCreateView.as_view(), name='order-add'),
    path('order_list/<pk>', OrderUpdateView.as_view(), name='order-update'),
    path('order_list/<pk>/delete', OrderDeleteView.as_view(), name='order-delete'),

    path('stock_list', StockList.as_view(), name='stock-list'),
    path('stock_list/add', StockCreateView.as_view(), name='stock-add'),
    path('stock_list/<pk>', StockUpdateView.as_view(), name='stock-update'),
    path('stock_list/<pk>/delete', StockDeleteView.as_view(), name='stock-delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

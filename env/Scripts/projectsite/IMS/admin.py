from django.contrib import admin
from .models import Product, Supplier, Warehouse, Order, Stock

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_number", "picture" ,"name", "description", "price")
    search_fields = ("name",)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "contact_no", "supplies")
    search_fields = ("name",)


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ("location", "name", "capacity", "display_products")  # Modify the list_display

    def display_products(self, obj):
        return ', '.join([product.name for product in obj.product_sto.all()])

    display_products.short_description = 'Products'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_number", "display_products", "order_date", "payment", "status")
    search_fields = ("order_number",)

    def display_products(self, obj):
        return ', '.join([product.name for product in obj.products.all()])

    display_products.short_description = 'Products'

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("stock_number", "product", "warehouse", "quantity", "expire_date")
    search_fields = ("product",)

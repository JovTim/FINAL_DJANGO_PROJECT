from django.core.management.base import BaseCommand
from ...models import Product, Supplier, Warehouse, Order, Stock

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_product()
        self.create_supplier()
        self.create_warehouse()
        self.create_order()
        self.create_stock()
    
    def create_product(self):
        product1 = Product(product_number=1, name="Electric Fan", description="Powerful cooling with adjustable settings.", price=500.00)
        product2 = Product(product_number=2, name="Smartphone", description="High-performance smartphone with AI capabilities.", price=899.99)
        product3 = Product(product_number=3, name="Coffee Maker", description="Programmable coffee maker for brewing your perfect cup.", price=120.00)
        product4 = Product(product_number=4, name="Yoga Mat", description="Non-slip yoga mat for comfortable exercise sessions.", price=35.50)
        product5 = Product(product_number=5, name="Bluetooth Speaker", description="Portable Bluetooth speaker with rich sound quality.", price=149.00)

        product_list = [product1, product2, product3, product4, product5]

        for product in product_list:
            product.save()

        self.stdout.write(self.style.SUCCESS('Successfully created Products'))

    def create_supplier(self):
        supplier1 = Supplier(supplier_number=1, name="DreamWare", email="dreamware_supplies@domain.com", contact_no="123-456-7890")
        supplier2 = Supplier(supplier_number=2, name="ZenithCorp", email="contact@zenithcorp.com", contact_no="987-654-3210")
        supplier3 = Supplier(supplier_number=3, name="NatureBloom", email="info@naturebloomproducts.com", contact_no="111-222-3333")
        supplier4 = Supplier(supplier_number=4, name="TechNova", email="sales@technova.net", contact_no="444-555-6666")
        supplier5 = Supplier(supplier_number=5, name="Globetech Solutions", email="hello@globetechsolutions.org", contact_no="777-888-9999")

        supplier_list = [supplier1, supplier2, supplier3, supplier4, supplier5]

        for supplier in supplier_list:
            supplier.save()
        
        self.stdout.write(self.style.SUCCESS('Successfully created Suppliers'))

    def create_warehouse(self):
        warehouse1 = Warehouse(location="Manila City, Philippines", name="Warehouse 1")
        warehouse2 = Warehouse(location="Puerto Princesa City, Palawan, Philippines", name="Warehouse 2")
        warehouse3 = Warehouse(location="New York City, USA", name="Warehouse 3")

        warehouse_list = [warehouse1, warehouse2, warehouse3]

        for warehouse in warehouse_list:
            warehouse.save()

        self.stdout.write(self.style.SUCCESS('Successfully created Warehouses'))

    def create_order(self):
        pass

    def create_stock(self):
        pass


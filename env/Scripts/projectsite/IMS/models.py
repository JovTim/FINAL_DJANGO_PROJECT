from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 

class Product(BaseModel):
    product_number = models.IntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to='images/', default='default_image.jpg')
    name = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class Supplier(BaseModel):
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    contact_no = models.CharField(max_length=250, null=True, blank=True)
    supplies = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Warehouse(BaseModel):
    location = models.CharField(max_length=150, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    product_sto = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

class Order(BaseModel):
    PAYMENT_METHOD = (
        ('Cash on Delivery', 'Cash on Delivery'),
        ('Credit/Debit Card', 'Credit/Debit Card'),
        ('GCash', 'GCash'),
    )

    STATUS = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Recieved', 'Recieved'),
        ('Cancelled', 'Cancelled'),
    )
    order_number = models.IntegerField(null=True, blank=True)
    products = models.ManyToManyField(Product)
    order_date = models.DateField(null=True, blank=True)
    payment = models.CharField(max_length=100, null=True, blank=True, choices=PAYMENT_METHOD)
    status = models.CharField(max_length=10, null=True, blank=True, choices=STATUS)

    def __str__(self):
        return str(self.order_number) if self.order_number else "No Order Number"

class Stock(BaseModel):
    stock_number = models.IntegerField(null=True, blank=True)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    expire_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.stock_number) if self.stock_number else "No Stock Number"


# Generated by Django 5.0 on 2023-12-28 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0005_remove_supplier_supplier_number_supplier_supplies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Shipped', 'Shipped'), ('Recieved', 'Recieved'), ('Cancelled', 'Cancelled')], max_length=10, null=True),
        ),
    ]

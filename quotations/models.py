from django.db import models
from django.utils import timezone
from sales.users.models import User
from datetime import datetime

class Quote(models.Model):
    customer_name = models.ForeignKey('customers.Customer',
        verbose_name='Contact Name',
        on_delete=models.CASCADE,
    )
    shipping_address1 = models.CharField(
        verbose_name='Shipping Address Line 1',
        max_length=200,
    )
    shipping_address2 = models.CharField(
        verbose_name='Shipping Address Line 2',
        max_length=200,
        blank=True,
    )
    shipping_postal = models.CharField(
        max_length=60,
        verbose_name='Shipping Postal',
    )
    created_by = models.ForeignKey(User,
        verbose_name='Created By',
    )
    created_date = models.DateTimeField(
        default=datetime.now,
    )
    is_confirmed = models.BooleanField(
        default=False,
    )
    TEMPLATE_CHOICES = (
        ('T1','Template 1: GST Excluded, Quantity Required, Total Shown'),
        ('T2','Template 2: GST Included, Quantity Required, Total Shown'),
        ('T3','Template 3: GST Excluded, Quantity Not Required'),
        ('T4','Template 4: GST Included, Quantity Not Required'),
    )
    template_type = models.CharField(
        max_length=2,
        choices=TEMPLATE_CHOICES,
        default='T3'
    )
    quote_total = models.DecimalField(
        verbose_name='Total',
        max_digits=20,
        decimal_places=2,
        default=0,
    )

    def __str__(self):
        return 'QuoteID: {} Customer:'.format(self.id, self.customer_name)

class Quote_Products(models.Model):
    quote_id = models.ForeignKey('Quote',
        verbose_name='Quote ID',
        on_delete=models.CASCADE,
    )
    product_name = models.ForeignKey('products.Product',
        verbose_name='Product Name',
        on_delete=models.CASCADE,
    )
    product_quantity = models.IntegerField(
        verbose_name='Product Quantity',
        blank=True,
        null=True,
    )
    product_price = models.DecimalField(
        verbose_name='Price',
        max_digits=20,
        decimal_places=2,
    )
    product_line_total = models.DecimalField(
        verbose_name='Line Total',
        max_digits=20,
        decimal_places=2,
        blank=True,
        null=True,
    )
    product_description = models.CharField(
        verbose_name='Product Description',
        max_length=200,
        blank=True,
    )

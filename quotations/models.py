from django.db import models
from django.utils import timezone
from sales.users.models import User
from datetime import datetime

class Quote(models.Model):
    customer_name = models.ForeignKey('customers.Customer',
        verbose_name='Customer Name',
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
    quote_total = models.BooleanField(
        default=False,
    )
    quote_gst = models.BooleanField(
        default=False,
    )
    is_confirmed = models.BooleanField(
        default=False,
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
    product_price = models.DecimalField(
        verbose_name='Price',
        max_digits=20,
        decimal_places=2,
    )
    product_description = models.CharField(
        verbose_name='Product Description',
        max_length=200,
        blank=True,
    )

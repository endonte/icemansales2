from django.db import models

class Category(models.Model):
    category_name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Category'
    )

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Product Name'
    )
    category = models.ForeignKey('Category',
        verbose_name='Category',
        on_delete=models.CASCADE
    )
    uom = models.CharField(
        max_length=200,
        verbose_name='UOM'
    )

    def __str__(self):
        return self.product_name

    def __unicode__(self):
        return 'Product {} in Category {}  with UOM ({})'.format(self.product_name, self.category, self.uom)

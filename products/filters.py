import django_filters as filters
from django_tables2 import SingleTableView
from .models import Product

class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'uom']
        order_by = ['pk']

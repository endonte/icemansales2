import django_tables2 as tables
from .models import Product

class ProductTable(tables.Table):
    category = tables.Column(accessor='category.category_name')
    class Meta:
        model = Product
        attrs = {'class': 'table-bordered table-hover'}

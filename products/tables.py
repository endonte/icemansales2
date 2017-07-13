import django_tables2 as tables
from django_tables2.utils import A
from .models import Product

class ProductTable(tables.Table):
#    pk = tables.LinkColumn('product-detail', args=[A('pk')])
    product_name = tables.LinkColumn('product-detail', args=[A('pk')])
    category = tables.LinkColumn('product-detail', args=[A('pk')])
    uom = tables.LinkColumn('product-detail', args=[A('pk')])

#    category = tables.Column(accessor='category.category_name')
    class Meta:
        model = Product
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no products matching the search criteria..."

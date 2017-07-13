from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query_utils import Q
from django_tables2 import RequestConfig
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from .tables import CustomerTable
from .filters import CustomerListFilter
from .utils import PagedFilteredTableView
from .models import Customer
from .forms import ProductListFormHelper

class ProductListView(LoginRequiredMixin, GroupRequiredMixin, PagedFilteredTableView):
    model = Product
    template_name = 'products/product.html'
    context_object_name = 'product'
    ordering = ['-id']
    group_required = u'company-user'
    table_class = ProductTable
    filter_class = ProductFilter
    formhelper_class = ProductListFormHelper

    def get_queryset(self):
        qs = super(ProductListView, self).get_queryset()
        return qs

    def post(self, request, *args, **kwargs):
        return PagedFilteredTableView.as_view()(request)

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['nav_product'] = True
        search_query = self.get_queryset()
        table = ProductTable(search_query)
        RequestConfig(self.request, paginate={'per_page': 25}).configure(table)
        context['table'] = table
        return context

from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.shortcuts import redirect
from django_tables2 import RequestConfig
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from .forms import ProductListFormHelper
from .models import Product
from .tables import ProductTable
from .filters import ProductFilter
from .utils import PagedFilteredTableView

class ProductListView(LoginRequiredMixin, PagedFilteredTableView):
    model = Product
    template_name = 'products/product.html'
    context_object_name = 'product'
    ordering = ['-id']
#    group_required = u'company-user'
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

#def product(request):
#    product_table = ProductTable(Product.objects.all())
#    RequestConfig(request, paginate={"per_page": 25, "page": 1}).configure(product_table)
#    return render(request, 'products/product.html', {
#        'product_table': product_table,
#        'category': Category.objects.all()
#    })

#def product(request):
#    if request.method == "POST":
#        product_form = ProductForm(request.POST)
#        if product_form.is_valid():
#            post = product_form.save(commit=False)
#            post.save()
#            return redirect('product')
#    else:
#        product_form = ProductForm()
#        queryset = Product.objects.select_related().all()
#        f = ProductFilter(request.GET, queryset=queryset)
#        product_table = ProductTable(f.qs)
#        RequestConfig(request, paginate={"per_page": 25, "page": 1}).configure(product_table)
#    return render(request, 'products/product.html', {
#        'product_table': product_table,
#        'filter': f,
#        'product_form': product_form
#        })

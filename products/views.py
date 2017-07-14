from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django_tables2 import RequestConfig, SingleTableView
from .forms import ProductForm
from .models import Product
from .tables import ProductTable
from .filters import ProductFilter, ProductFilterEx

#def product(request):
#    product_table = ProductTable(Product.objects.all())
#    RequestConfig(request, paginate={"per_page": 25, "page": 1}).configure(product_table)
#    return render(request, 'products/product.html', {
#        'product_table': product_table,
#        'category': Category.objects.all()
#    })

def product(request):
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            post = product_form.save(commit=False)
            post.save()
            return redirect('product')
    else:
        product_form = ProductForm()
        queryset = Product.objects.select_related().all()
        f = ProductFilter(request.GET, queryset=queryset)
        product_table = ProductTable(f.qs)
        RequestConfig(request, paginate={"per_page": 25, "page": 1}).configure(product_table)
    return render(request, 'products/product.html', {
        'product_table': product_table,
        'filter': f,
        'product_form': product_form
        })


class FilterExListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(FilterExListView, self).get_context_data(**kwargs)
        filter = ProductFilterEx(self.request.GET, queryset=self.object_list)

        table = ProductTable(filter.qs)
        RequestConfig(self.request, ).configure(table )

        context['filter'] = filter
        context['table'] = table

        return context

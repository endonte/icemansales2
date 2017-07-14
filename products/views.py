from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import ModelFormMixin
from django_tables2 import RequestConfig, SingleTableView
from .forms import ProductForm
from .models import Product
from .tables import ProductTable
from .filters import ProductFilterEx


class FilterExListView(ListView, ModelFormMixin):
    model = Product
    form_class = ProductForm

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        # Explicitly states what get to call:
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # When the form is submitted, it will enter here
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save()
            self.form = self.get_form(self.form_class)
            # Here ou may consider creating a new instance of form_class(),
            # so that the form will come clean.

        # Whether the form validates or not, the view will be rendered by get()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(FilterExListView, self).get_context_data(*args, **kwargs)
        filter = ProductFilterEx(self.request.GET, queryset=self.object_list)

        table = ProductTable(filter.qs)
        RequestConfig(self.request, ).configure(table )

        context['filter'] = filter
        context['table'] = table
        context['form'] = self.form

        return context

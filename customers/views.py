from django.views.generic import ListView
from django.shortcuts import render
from django.views.generic.edit import ModelFormMixin
from django_tables2 import RequestConfig
from .forms import CustomerForm
from .models import Customer

# Create your views here.
#def customer_list(request):
#    return render(request, 'customers/customer_list.html', {})

class CustomerListView(ListView, ModelFormMixin):
    model = Customer
    form_class = CustomerForm

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
            # Here you may consider creating a new instance of form_class(),
            # so that the form will come clean.

        # Whether the form validates or not, the view will be rendered by get()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(CustomerListView, self).get_context_data(*args, **kwargs)

        context['form'] = self.form

        return context

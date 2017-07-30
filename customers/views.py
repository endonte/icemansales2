from django.views.generic import ListView
from django.views.generic.edit import ModelFormMixin
from django_tables2 import RequestConfig
from django.utils import timezone
from sales.users.models import User
from .forms import CustomerForm, LeadForm
from .models import Customer


class CustomerListView(ListView, ModelFormMixin):
    model = Customer
    form_class = CustomerForm
    template_name='customers/customer_list.html'

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
            self.object = self.form.save(commit=False)
            self.object.customer_created_by = request.user
            self.object.customer_created_by_date = timezone.now()
            self.object.save()
            self.form = self.get_form(self.form_class)
            # Here you may consider creating a new instance of form_class(),
            # so that the form will come clean.

        # Whether the form validates or not, the view will be rendered by get()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(CustomerListView, self).get_context_data(*args, **kwargs)

        context['customers'] = Customer.objects.all()
        context['form'] = self.form

        return context

class LeadListView(ListView, ModelFormMixin):
    model = Customer
    form_class = LeadForm
    template_name='customers/lead_list.html'

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
        context = super(LeadListView, self).get_context_data(*args, **kwargs)

        context['form'] = self.form

        return context

from django.shortcuts import render
from django.views.generic.edit import ModelFormMixin
from django.views.generic import ListView
from .models import Quote, Quote_Products
from .forms import QuoteForm
# Create your views here.

class CreateQuotation(ListView, ModelFormMixin):
    model = Quote
    form_class = QuoteForm
    template_name='quotations/create_quotation.html'

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
        context = super(CreateQuotation, self).get_context_data(*args, **kwargs)

        context['form'] = self.form

        return context

class QuotationList(ListView):
    model = Quote
    template_name='quotations/quotation_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(QuotationList, self).get_context_data(*args, **kwargs)

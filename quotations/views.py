from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic.edit import ModelFormMixin
from django.views.generic import ListView
from django.utils import timezone
from django.http import HttpResponseRedirect
from sales.users.models import User
from .models import Quote, Quote_Products
from .forms import QuoteForm, QuoteProductForm

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
            self.object = self.form.save(commit=False)
            self.object.created_by = request.user
            self.object.created_date = timezone.now()
            self.object.save()

            #return redirect('create_quotation_add_product', kwargs={'pk': self.object.pk})
            return redirect('create_quotation_add_product', kwargs={'pk': self.object.pk})
            #self.form = self.get_form(self.form_class)
            # Here you may consider creating a new instance of form_class(),
            # so that the form will come clean.

        # Whether the form validates or not, the view will be rendered by get()
        return self.get(request, *args, **kwargs)
        #return HttpResponseRedirect(reverse(QuotationAddProduct, args=(self.object.pk,)))
        #return QuotationAddProduct.as_view()(request)

    def get_context_data(self, *args, **kwargs):
        context = super(CreateQuotation, self).get_context_data(*args, **kwargs)
        #context['quote_pk'] = self.object.objects.get(pk=self.kwargs['pk'])
        context['form'] = self.form
        return context

class QuotationList(ListView):
    model = Quote
    template_name='quotations/quotation_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(QuotationList, self).get_context_data(*args, **kwargs)

class QuotationAddProduct(ListView, ModelFormMixin):
    model = Quote_Products
    form_class = QuoteProductForm
    template_name='quotations/quotation_add_products.html'

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
            self.object.quote_id = Quote.objects.get(pk=self.kwargs['pk'])
            self.object.save()

            self.form = self.get_form(self.form_class)
            # Here you may consider creating a new instance of form_class(),
            # so that the form will come clean.

        # Whether the form validates or not, the view will be rendered by get()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(QuotationAddProduct, self).get_context_data(*args, **kwargs)

        context['form'] = self.form
        context['quote_pk'] = Quote.objects.get(pk=self.kwargs['pk'])
        context['quote_products'] = Quote_Products.objects.filter(
            quote_id=Quote.objects.get(pk=self.kwargs['pk'])
        )

        return context

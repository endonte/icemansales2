from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic.edit import ModelFormMixin
from django.views.generic import ListView, View
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from sales.users.models import User
from .models import Quote, Quote_Products
from .forms import QuoteForm, QuoteProductForm
from reportlab.pdfgen import canvas
from .utils import render_to_pdf


class CreateQuotation(ListView, ModelFormMixin):
    model = Quote
    form_class = QuoteForm
    template_name='quotations/create_quotation.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save(commit=False)
            self.object.created_by = request.user
            self.object.created_date = timezone.now()
            self.object.save()

            return HttpResponseRedirect(reverse('create_quotation_add_product', args=(self.object.pk,)))

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

class QuotationAddProduct(ListView, ModelFormMixin):
    model = Quote_Products
    form_class = QuoteProductForm
    template_name='quotations/quotation_add_products.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save(commit=False)
            self.object.quote_id = Quote.objects.get(pk=self.kwargs['pk'])
            self.object.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(QuotationAddProduct, self).get_context_data(*args, **kwargs)

        context['form'] = self.form
        context['quote_pk'] = Quote.objects.get(pk=self.kwargs['pk'])
        context['quote_products'] = Quote_Products.objects.filter(
            quote_id=Quote.objects.get(pk=self.kwargs['pk'])
        )

        return context

class QuotationTemplate1(ListView):
    model = Quote_Products
    template_name = 'quotations/quotation_template1.html'

    def get_context_data(self, *args, **kwargs):
        context = super(QuotationTemplate1, self).get_context_data(*args, **kwargs)

        context['quote_pk'] = Quote.objects.get(pk=self.kwargs['pk'])
        context['quote_products'] = Quote_Products.objects.filter(
            quote_id=Quote.objects.get(pk=self.kwargs['pk'])
        )

        return context


class PrintView(View):
    def get(self, request, *args, **kwargs):
        data = {
            'quote_pk': Quote.objects.get(pk=self.kwargs['pk']),
            'quote_products': Quote_Products.objects.filter(
                    quote_id=Quote.objects.get(pk=self.kwargs['pk'])
                    ),
        }
        pdf = render_to_pdf('quotations/pdf/quotation-pdf-1.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

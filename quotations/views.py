from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic.edit import ModelFormMixin
from django.views.generic import ListView, View
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from sales.users.models import User
from .models import Quote, Quote_Products
from .forms import QuoteForm, QuoteProductForm1, QuoteProductForm2
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

        context['quote_pk'] = Quote.objects.all()

        return context

class QuotationAddProduct(ListView, ModelFormMixin):
    model = Quote_Products
    form_class = QuoteProductForm1
    template_name='quotations/quotation_add_products.html'

    def form_type(self, *args, **kwargs):
        quote_id = Quote.objects.get(pk=self.kwargs['pk'])
        template = quote_id.template_type
        if template == 'T3' or template == 'T4':
            self.form_class = QuoteProductForm1
        elif template == 'T1' or template == 'T2':
            self.form_class = QuoteProductForm2

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form_type(Quote.objects.get(pk=self.kwargs['pk']))
        self.form = self.get_form(self.form_class)
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form_type(Quote.objects.get(pk=self.kwargs['pk']))
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save(commit=False)
            self.object.quote_id = Quote.objects.get(pk=self.kwargs['pk'])
            if self.object.product_quantity:
                self.object.product_line_total = self.object.product_quantity * self.object.product_price

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


class QuotationTemplate(ListView):
    model = Quote_Products
    template_name = 'quotations/quotation_template.html'

    def get_context_data(self, *args, **kwargs):
        context = super(QuotationTemplate, self).get_context_data(*args, **kwargs)

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
        instance = Quote.objects.get(pk=self.kwargs['pk'])
        if instance.template_type == 'T1':
            pdf = render_to_pdf('quotations/pdf/quotation-pdf-1.html', data)
        elif instance.template_type == 'T2':
            pdf = render_to_pdf('quotations/pdf/quotation-pdf-2.html', data)
        elif instance.template_type == 'T4':
            pdf = render_to_pdf('quotations/pdf/quotation-pdf-4.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

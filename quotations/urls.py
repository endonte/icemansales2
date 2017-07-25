from django.conf.urls import url
from .views import CreateQuotation, QuotationList, QuotationAddProduct, QuotationTemplate1, PrintView
from . import views

urlpatterns = [
    url(r'^quotation_list/$', QuotationList.as_view(), name='quotation_list'),
    url(r'^create_quotation/$', CreateQuotation.as_view(), name='create_quotation'),
    url(r'^create_quotation/quotation-id-(?P<pk>\d+)/$',
        QuotationAddProduct.as_view(),
        name='create_quotation_add_product'
    ),
    url(r'^quotation_list/1/quotation-id-(?P<pk>\d+)/$',
        QuotationTemplate1.as_view(),
        name='quotation_template_1'
    ),
    url(r'^quotation_list/quotation-id-(?P<pk>\d+)/$', PrintView.as_view(), name='pdf_printer'),
]

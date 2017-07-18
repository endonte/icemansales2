from django.conf.urls import url
from .views import CreateQuotation, QuotationList, QuotationAddProduct

urlpatterns = [
    url(r'^quotation_list/$', QuotationList.as_view(), name='quotation_list'),
    url(r'^create_quotation/$', CreateQuotation.as_view(), name='create_quotation'),
    url(r'^create_quotation/quotation-id-(?P<pk>\d+)/$',
        QuotationAddProduct.as_view(),
        name='create_quotation_add_product'
    ),
]

from django.conf.urls import url
from .views import CreateQuotation, QuotationList

urlpatterns = [
    url(r'^quotation_list/$', QuotationList.as_view(), name='quotation_list'),
    url(r'^create_quotation/$', CreateQuotation.as_view(), name='create_quotation'),
]

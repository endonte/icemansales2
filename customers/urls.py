from django.conf.urls import url
from .views import CustomerListView, LeadListView

urlpatterns = [
    url(r'^customer_list/$', CustomerListView.as_view(), name='customer_list'),
    url(r'^lead_list/$', LeadListView.as_view(), name='lead_list'),
]

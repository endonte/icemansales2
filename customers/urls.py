from django.conf.urls import url
from .views import CustomerListView

urlpatterns = [
    url(r'^customer_list/$', CustomerListView.as_view(), name='customer_list'),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^customer_list/$', views.customer_list, name='customer_list'),
]

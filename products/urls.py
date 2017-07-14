from django.conf.urls import url
from . import views
from .views import FilterExListView

urlpatterns = [
    url(r'^product_list/$', FilterExListView.as_view(), name='product_list'),
]

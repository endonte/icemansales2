from django.conf.urls import url
from . import views
from .views import FilterExListView

urlpatterns = [
    url(r'product/', views.product, name='product'),
    url(r'^product_list/$', FilterExListView.as_view() ),
]

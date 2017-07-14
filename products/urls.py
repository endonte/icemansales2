from django.conf.urls import url
from .views import ProductListView

urlpatterns = [
    url(r'^product/$', ProductListView.as_view(), name='product'),
]

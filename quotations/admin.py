from django.contrib import admin
from .models import Quote, Quote_Products

my_models = [Quote, Quote_Products]
admin.site.register(my_models)

from django.contrib import admin
from .models import Customer

# Register your models here.
my_models = [Customer]
admin.site.register(my_models)

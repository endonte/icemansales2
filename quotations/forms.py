from django import forms
from .models import Quote, Quote_Products

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = (
                'customer_name',
                'shipping_address1',
                'shipping_address2',
                'shipping_postal',
                'quote_total',
                'quote_gst',
                'template_type',
            )
        #widgets = {
        #    'template_type': RadioSelect,
        #}

class QuoteProductForm(forms.ModelForm):
    class Meta:
        model = Quote_Products
        fields = (
                'product_name',
                'product_price',
                'product_description',
        )

class LockQuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('is_confirmed',)

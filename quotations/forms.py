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
                'template_type',
            )


class QuoteProductForm1(forms.ModelForm):
    class Meta:
        model = Quote_Products
        fields = (
                'product_name',
                'product_price',
                'product_description',
        )

class QuoteProductForm2(forms.ModelForm):
    class Meta:
        model = Quote_Products
        fields = (
                'product_name',
                'product_price',
                'product_quantity',
                'product_description',
        )

class LockQuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('is_confirmed',)

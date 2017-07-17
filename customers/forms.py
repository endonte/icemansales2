from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
                'contact',
                'contact_email',
                'contact_num',
                'business_name',
                'business_reg_no',
                'billing_address_1',
                'billing_address_2',
                'billing_postal',
            )

class LeadForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
                'contact',
                'contact_email',
                'contact_num',
                'business_name',
                'business_reg_no',
                'billing_address_1',
                'billing_address_2',
                'billing_postal',
            )

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_forms.bootstrap import InlineField, StrictButton, FormActions
from .models import Product

#class ProductForm(forms.ModelForm):
#    class Meta:
#        model = Product
#        fields = ('category', 'product_name', 'uom',)

class ProductListFormHelper(FormHelper):
    form_id = 'product-search-form'
    form_class = 'form-inline'
    field_template = 'bootstrap3/layout/inline_field.html'
    field_class = 'col-xs-3'
    label_class = 'col-xs-3'
    form_show_errors = True
    help_text_inline = False
    html5_required = True
    layout = Layout(
                Fieldset(
                    '<i class="fa fa-search"></i> Search Products',
                    InlineField('product_name'),
                    InlineField('category'),
                    InlineField('uom'),
                ),
                FormActions(
                    StrictButton(
                        '<i class="fa fa-search"></i> Search',
                        type='submit',
                        css_class='btn-primary',
                        style='margin-top:10px;')
                )
    )

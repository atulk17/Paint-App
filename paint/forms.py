from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class SearchDistributorForm(forms.Form):
    Distributor_name = forms.CharField(required=False)
    phone = forms.CharField(required=False)

class SearchCustomerForm(forms.Form):
    customer_name = forms.CharField(required=False)
    phone = forms.CharField(required=False)

class SearchProductForm(forms.Form):
    product_name = forms.CharField(required=False)
    



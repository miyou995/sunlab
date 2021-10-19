from django import forms 
from django.forms import NumberInput
# from django.core import validators

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField( min_value=1, widget=NumberInput(attrs={'class': 'form-control text-center','value': 1, 'max':20 }))
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    parfum   = forms.CharField(max_length=20, required=False)
    cheveux  = forms.CharField(max_length=20, required=False)

class CartAddProductQuantityForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)


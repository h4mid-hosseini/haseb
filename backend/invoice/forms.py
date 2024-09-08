from django import forms
from django.forms import inlineformset_factory
from . import models


class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = models.InvoiceItem
        fields = ['title', 'price', 'quantity']




class InvoiceForm(forms.ModelForm):
    class Meta:
        model = models.Invoice
        fields = ['owner']  # Don't include items directly

InvoiceItemFormset = inlineformset_factory(
    models.Invoice,  # Parent model
    models.InvoiceItem,  # Child model
    form=InvoiceItemForm,
    extra=1,
    can_delete=True
)

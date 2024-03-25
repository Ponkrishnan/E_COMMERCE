from django import forms
from .models import index

class CustomerDetailForm(forms.ModelForm):
    class Meta:
        model = index
        fields = ['name', 'email', 'subject', 'message']
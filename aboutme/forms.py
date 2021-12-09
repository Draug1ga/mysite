from django.forms import ModelForm
from aboutme.models import Messageme
from django import forms

class MessagemeForm(ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(
        attrs={
           'class':'form-control',
            'placeholder': 'First name',
        }))
    last_name=forms.CharField(widget=forms.TextInput(
        attrs={
           'class':'form-control',
            'placeholder': 'Last name',
        }))
    email_address=forms.CharField(widget=forms.TextInput(
        attrs={
           'class':'form-control',
            'placeholder': 'Email address',
        }))
    message = forms.CharField(widget=forms.TextInput(
        attrs={
           'class':'form-control',
            'placeholder': 'Message',
        }))

    class Meta:
        model = Messageme
        fields = ['first_name','last_name','email_address','message']
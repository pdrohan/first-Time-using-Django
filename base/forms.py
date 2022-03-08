from django import forms
from phone_field import PhoneField

class ContactForm(forms.Form):
    name    = forms.CharField(max_length=100)
    email   = forms.EmailField()
    phone   = PhoneField(blank=True, help_text='Contact phone number')
    message = forms.CharField(widget=forms.Textarea)

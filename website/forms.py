from django import forms
from website.models import Contact , Email

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'

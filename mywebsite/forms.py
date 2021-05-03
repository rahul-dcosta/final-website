from django import forms

class contactForm(forms.Form):
    fromemail=forms.EmailField(required=True)
    subject=forms.CharField(required=True)
    message=forms.ChaarField(required=True)

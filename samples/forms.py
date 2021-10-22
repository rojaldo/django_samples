from django import forms

class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label='Nombre')
    email = forms.EmailField(required=False, label='Email')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

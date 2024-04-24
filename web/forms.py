from django import forms
from .models import ContactForm, Flan

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email','customer_name','message']
        labels = {
            'customer_email': 'Correo electrónico',
            'customer_name': 'Nombre',
            'message': 'Mensaje'}

class FlanForm(forms.ModelForm):
    class Meta:
        model = Flan
        fields = ['name', 'description','price_clp','image_url', 'is_private']

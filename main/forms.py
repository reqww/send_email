from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    '''Форма подписки на рассылку по email'''
    class Meta:
        model = Contact
        fields = '__all__'
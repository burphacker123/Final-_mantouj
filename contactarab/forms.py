from django import forms
from .models import contact

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ('الاسم', 'اسم_العائلة', 'البريد_الإلكتروني', 'المنتج', 'رسالة')
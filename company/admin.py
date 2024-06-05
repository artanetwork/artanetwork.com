from django import forms
from django.contrib import admin

from .models import Company

# Register your models here.


class CustomForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'phone': forms.TextInput(
                attrs={
                    'class': 'vTextField',
                    'style': 'direction: ltr;',
                    'placeholder': '+۹۸ ۲۱ ۱۲۳۴ ۵۶۷۸',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'vTextField',
                    'style': 'direction: ltr;',
                    'placeholder': 'info@company.com',
                }
            ),
        }


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    form = CustomForm
    list_display = (
        'name',
        'phone',
        'email',
    )

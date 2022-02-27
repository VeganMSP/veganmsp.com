from dal.autocomplete import ModelSelect2
from django.forms import ModelForm, Textarea

from .models import (
    Restaurant,
    VeganCompany
)


class RestaurantModelForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = (
            'name',
            'location',
            'website',
            'description',
            'all_vegan',
        )
        widgets = {
            'description': Textarea(
                attrs={
                    'rows': 15,
                    'cols': 84,
                    'style': 'font-family: monospace'
                }
            ),
            'location': ModelSelect2(url='info:city-autocomplete')
        }


class VeganCompanyModelForm(ModelForm):
    class Meta:
        model = VeganCompany
        fields = (
            '__all__'
        )
        widgets = {
            'description': Textarea(
                attrs={
                    'rows': 15,
                    'cols': 84,
                    'style': 'font-family: monospace'
                }
            ),
        }

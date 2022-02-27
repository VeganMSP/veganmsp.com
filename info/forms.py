from dal.autocomplete import ModelSelect2
from django.forms import ModelForm, Textarea

from .models import (
    Address,
    FarmersMarket,
    Link,
    LinkCategory,
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


class FarmersMarketModelForm(ModelForm):
    class Meta:
        model = FarmersMarket
        fields = (
            'name',
            'website',
            'phone',
            'hours',
        )
        exclude = ('address',)
        widgets = {
            'hours': Textarea(
                attrs={
                    'rows': 15,
                    'cols': 64,
                    'style': 'font-family: monospace'
                }
            ),
        }


class AddressModelForm(ModelForm):
    class Meta:
        model = Address
        fields = (
            '__all__'
        )
        widgets = {
            'city': ModelSelect2(url='info:city-autocomplete')
        }


class LinkModelForm(ModelForm):
    class Meta:
        model = Link
        fields = (
            '__all__'
        )
        exclude = ('category',)


class LinkCategoryModelForm(ModelForm):
    class Meta:
        model = LinkCategory
        fields = (
            '__all__'
        )

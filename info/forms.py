from dal.autocomplete import ModelSelect2
from django.forms import (
    BooleanField,
    ModelForm,
    Textarea,
    TextInput,
)

from .models import (
    Address,
    FarmersMarket,
    Link,
    LinkCategory,
    Restaurant,
    VeganCompany
)


class BaseRestaurantForm(ModelForm):
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
            'name': TextInput(
                attrs={
                    'autofocus': True,
                }
            ),
            'description': Textarea(
                attrs={
                    'rows': 15,
                    'cols': 84,
                    'style': 'font-family: monospace'
                }
            ),
            'location': ModelSelect2(url='info:city-autocomplete')
        }


class RestaurantAddForm(BaseRestaurantForm):
    add_another = BooleanField(required=False)

    class Meta:
        model = BaseRestaurantForm.Meta.model
        fields = BaseRestaurantForm.Meta.fields + ('add_another',)
        widgets = {
            'name': TextInput(
                attrs={
                    'autofocus': True,
                }
            ),
            'description': Textarea(
                attrs={
                    'rows': 15,
                    'cols': 84,
                    'style': 'font-family: monospace'
                }
            ),
            'location': ModelSelect2(url='info:city-autocomplete')
        }


class BaseVeganCompanyForm(ModelForm):
    class Meta:
        model = VeganCompany
        fields = (
            'name',
            'website',
            'description',
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


class VeganCompanyAddForm(BaseVeganCompanyForm):
    add_another = BooleanField(required=False)

    class Meta:
        model = BaseVeganCompanyForm.Meta.model
        fields = BaseVeganCompanyForm.Meta.fields + ('add_another',)
        widgets = {
            'name': TextInput(
                attrs={
                    'autofocus': True,
                }
            ),
            'description': Textarea(
                attrs={
                    'rows': 15,
                    'cols': 84,
                    'style': 'font-family: monospace'
                }
            ),
        }


class BaseFarmersMarketForm(ModelForm):
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


class FarmersMarketAddForm(BaseFarmersMarketForm):
    add_another = BooleanField(required=False)

    class Meta:
        model = BaseFarmersMarketForm.Meta.model
        fields = BaseFarmersMarketForm.Meta.fields + ('add_another',)
        widgets = {
            'name': TextInput(
                attrs={
                    'autofocus': True,
                }
            ),
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


class BaseLinkForm(ModelForm):
    class Meta:
        model = Link
        fields = (
            'name',
            'website',
            'description',
        )
        exclude = ('category',)
        widgets = {
            'name': TextInput(
                attrs={
                    'autofocus': True,
                }
            ),
        }


class LinkAddForm(BaseLinkForm):
    add_another = BooleanField(required=False)

    class Meta:
        model = BaseLinkForm.Meta.model
        fields = BaseLinkForm.Meta.fields + ('add_another',)
        widgets = {
            'name': TextInput(
                attrs={
                    'autofocus': True,
                }
            ),
        }


class LinkCategoryModelForm(ModelForm):
    class Meta:
        model = LinkCategory
        fields = (
            '__all__'
        )

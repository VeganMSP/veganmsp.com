from typing import Text
from django.forms import ModelForm, Textarea

from .models import Restaurant


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
			)
		}
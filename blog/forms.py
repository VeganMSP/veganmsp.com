from dal.autocomplete import ModelSelect2
from django.forms import Textarea

from generic.forms import CustomForm

from .models import Post


class PostModelForm(CustomForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'status',
            'category',
        )
        widgets = {
            'content': Textarea(
                attrs={
                    'rows': 30,
                    'cols': 84,
                    'style': 'font-family: monospace'
                }),
            'category': ModelSelect2(url='blog:category-autocomplete'),
        }

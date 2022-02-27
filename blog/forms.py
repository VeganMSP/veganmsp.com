from dal.autocomplete import ModelSelect2
from django.forms import ModelForm, Textarea

from .models import Post


class PostModelForm(ModelForm):
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

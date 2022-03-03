from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter()
@stringfilter
def html_arrows(value):
    return value.replace("->", '&raquo;')

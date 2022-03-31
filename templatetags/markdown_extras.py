from django import template
from django.template.defaultfilters import stringfilter

import markdown2 as md

register = template.Library()

MARKDOWN_EXTRAS = [
    'fenced-code-blocks',
    'tables',
    'footnotes',
    'header-ids',
    'strike',
]


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extras=MARKDOWN_EXTRAS)

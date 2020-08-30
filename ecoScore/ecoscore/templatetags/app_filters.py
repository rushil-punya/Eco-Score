from django import template
register = template.Library()

from ..models import Cell

@register.filter(name='callButtonClick')
def callButtonClick(value):
    value = True
    return value

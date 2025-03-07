import markdown
from django import template 
from django.utils.safestring import mark_safe 

register = template.Library()

@register.filter()
def mark(value):
    extentions = ['nl2br', 'fenced_code', 'codehilite']
    return mark_safe(markdown.markdown(value, extentions=extentions))
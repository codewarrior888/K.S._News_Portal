from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag()
def current_date(format_string='%d.%b.%Y'):
    return datetime.utcnow().strftime(format_string)


# @register.simple_tag
# def current_time(format_string):
#     return datetime.datetime.now().strftime(format_string)

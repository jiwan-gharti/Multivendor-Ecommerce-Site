from django import template
register = template.Library()

from datetime import date

@register.filter(name='today_date')
def today_date():
    print(date.today)
    return date.today

@register.filter(name='today_date')
def today_date():
    print(date.today+7)
    return date.today + 7
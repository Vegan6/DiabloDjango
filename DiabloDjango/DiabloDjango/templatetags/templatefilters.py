from django import template
from datetime import date, datetime, timedelta

register = template.Library()

@register.filter(name='frommillisec')
def frommillisec(value):
    seconds=(value/1000)%60
    seconds = int(seconds)
    minutes=(value/(1000*60))%60
    minutes = int(minutes)
    return ("%dm:%ds" % (minutes, seconds))
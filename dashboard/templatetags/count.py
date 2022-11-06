import datetime

from dashboard.models import GuestLocation
from django import template

register = template.Library()


@register.filter()
def visitors(QuerySet):
    return QuerySet.count()


@register.filter(name="latest", is_safe=True)
def since_last_week_visitors(QuerySet):
    today = datetime.datetime.today()
    first_d_o_w = datetime.timedelta(
        days=datetime.datetime.today().isoweekday() % 7)

    return GuestLocation.objects.filter(date__gt=today-first_d_o_w).count()

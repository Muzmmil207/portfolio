from django import template
from dashboard.models import GuestLocation
import datetime

register = template.Library()


@register.filter()
def visitors(QuerySet):
    return QuerySet.count()


@register.filter(name="latest", is_safe=True)
def since_last_week_visitors(QuerySet):
    today = datetime.datetime.today()
    first_d_o_w = datetime.timedelta(
        days=datetime.datetime.today().isoweekday() % 7)

    return len(GuestLocation.objects.filter(date__gt=today-first_d_o_w))

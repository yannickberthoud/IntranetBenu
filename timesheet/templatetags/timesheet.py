from django import template
from django.db.models import Q

from timesheet.models import Timesheet
import datetime

register = template.Library()

@register.inclusion_tag('timesheet/latest_timesheet.html', takes_context=True)
def show_my_timesheet(context):
    request = context['request']
    timesheets = Timesheet.objects.filter(owner = request.user.pk, week = datetime.datetime.now().isocalendar()[1]).order_by('-working_hour')[:10]
    return {'timesheets': timesheets}


@register.inclusion_tag('timesheet/latest_timesheet.html', takes_context=True)
def show_timesheet_of(context, id):
    request = context['request']
    timesheets = Timesheet.objects.filter(owner = id, week = datetime.datetime.now().isocalendar()[1]).order_by('-working_hour')[:10]
    return {'timesheets': timesheets}
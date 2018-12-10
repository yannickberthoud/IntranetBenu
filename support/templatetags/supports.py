from django import template

from support.models import HelpDesk

register = template.Library()

@register.inclusion_tag('support/helpdesk/critical_tickets.html', takes_context=True)
def show_my_critical_tickets(context):
    request = context['request']
    tickets = HelpDesk.objects.filter(assigned_to = request.user.pk, priority = 'c', status = 'o').order_by('created_at')[:10]
    return {'tickets': tickets}
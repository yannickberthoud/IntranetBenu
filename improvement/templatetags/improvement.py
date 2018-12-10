from django import template
from django.db.models import Q

from improvement.models import Improvement

register = template.Library()

@register.inclusion_tag('improvement/latest_improvement.html', takes_context=True)
def show_latest_improvement(context):
    request = context['request']
    improvements = Improvement.objects.filter(~Q( status = 'D', progress = 100)).order_by('created_at')[:10]
    return {'improvements': improvements}
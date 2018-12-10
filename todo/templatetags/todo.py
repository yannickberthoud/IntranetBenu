from django import template

from todo.models import Todo

register = template.Library()

@register.inclusion_tag('todo/critical_tasks.html', takes_context=True)
def show_my_critical_tasks(context):
    request = context['request']
    tasks = Todo.objects.filter(assigned_to = request.user.pk, status = 'o').order_by('-due_date')[:10]
    return {'tasks': tasks}

@register.inclusion_tag('todo/show_tasks_of.html', takes_context=True)
def show_tasks_of(context, id):
    return {'tasks': Todo.objects.filter(assigned_to = id, status = 'o').order_by('-due_date')}
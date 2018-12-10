from django.db import models
from employee.models import User
from django.utils.translation import ugettext_lazy as _


def newManagerTasks(pharmacy_name):
    pass

class Todo(models.Model):
    CATEGORIES = (
        ('I', 'IT'),
    )
    PRIORITIES = (
        ('l', _('Low')),
        ('n', _('Normal')),
        ('h', _('Hight')),
        ('c', _('Critical'))
    )
    STATUS = (
        ('o', _("open")),
        ('s', _("Close: solved")),
        ('a', _('Close: abandon')),
    )
    department = models.CharField(max_length = 1, verbose_name = _("Category"), choices = CATEGORIES)
    assigned_to = models.ForeignKey(User, on_delete = models.CASCADE, blank = True)
    priority = models.CharField(max_length = 1, verbose_name = _("Priority"), choices = PRIORITIES)
    title = models.CharField(max_length = 64)
    description = models.CharField(max_length = 64)
    due_date = models.DateTimeField()
    status = models.CharField(max_length = 1, verbose_name = _("Status"), choices = STATUS)

    def __str__(self):
        return self.title
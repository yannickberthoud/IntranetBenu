from django.db import models
from employee.models import User
from django.utils.translation import ugettext_lazy as _

class HelpDesk(models.Model):
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
    assigned_to = models.ForeignKey(User, on_delete = models.CASCADE)
    client = models.CharField(max_length = 64, verbose_name = _("Client"))
    priority = models.CharField(max_length = 1, verbose_name = _("Priority"), choices = PRIORITIES)
    category = models.CharField(max_length = 1, verbose_name = _("Category"), choices = CATEGORIES)
    description_of_the_problem = models.TextField(verbose_name = _("Description of the problem"))
    followed = models.TextField(verbose_name = _("Followed"), blank = True)
    solution = models.TextField(verbose_name = _("Solution"), blank = True)
    status = models.CharField(max_length = 1, verbose_name = _("Status"), choices = STATUS)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return _("{} assigned to: {} - priority: {} - created at: {} - last update at: {}").format(self.client, self.assigned_to, self.priority, self.created_at, self.updated_at)

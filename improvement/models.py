from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator

from employee.models import User

class Improvement(models.Model):
    STATUS_CHOICES = (
        ('A', _('Abandoned')),
        ('D', _('Deployed')),
        ('P', _('Development in progress')),
        ('W', _('Waiting')),
    )
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    module = models.CharField(max_length = 64)
    title = models.CharField(max_length = 64)
    description = models.TextField()
    advancement = models.TextField(blank = True)
    is_approved = models.BooleanField(default = False)
    status = models.CharField(max_length = 1, choices = STATUS_CHOICES, default='W')
    progress = models.PositiveIntegerField(default= 0, validators=[MaxValueValidator(100),])
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title

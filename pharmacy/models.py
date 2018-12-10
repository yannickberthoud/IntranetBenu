from django.db import models
from django.utils.translation import ugettext_lazy as _

from contact.models import Contact
from employee.models import User
from todo.models import newManagerTasks

class Pharmacy(Contact):
    manager = models.ForeignKey(User, on_delete = models.PROTECT)
    uuid = models.CharField(max_length = 64, unique = True)
    name = models.CharField(max_length = 64)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'pharmacies'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.uuid = "{}{}".format(self.pk, self.manager.pk)
        if not self.uuid:
            newManagerTasks(self.name)
        super(Pharmacy, self).save(*args, **kwargs)

    

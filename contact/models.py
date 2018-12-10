from django.db import models
from django.utils.translation import ugettext_lazy as _

class Contact(models.Model):
    street = models.CharField(max_length = 128, verbose_name = _("Street"))
    npa = models.PositiveIntegerField(verbose_name = _("NPA"))
    city = models.CharField(max_length = 64, verbose_name = _("City"))
    canton = models.CharField(max_length = 64, verbose_name = _("Canton"))
    phone = models.IntegerField(blank = True, null = True)
    fax = models.IntegerField(blank = True, null = True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.street

from django.db import models
from employee.models import User
from django.utils.translation import ugettext_lazy as _

import datetime
import time
from datetime import date

class Timesheet(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 64, verbose_name = _("Title"))
    date = models.DateField(default=datetime.datetime.now())
    working_hour = models.FloatField(verbose_name = _("Working time"))
    week = models.IntegerField(verbose_name = "working week")

    def __str__(self):
        return "{}".format(self.title)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.week = datetime.datetime.strptime("{}".format(self.date), "%Y-%m-%d").isocalendar()[1]
        super(Timesheet, self).save(*args, **kwargs)

def user_directory_path(self, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(self.user.id, filename)

class ExpanseReport(models.Model):
    CATEGORIES = (
        ('M', _('Meal')),
        ('T', _('Travel')),
        ('H', _('Hotel')),
        ('O', _('Other')),
    )
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField()
    category = models.CharField(max_length = 1, verbose_name = _("Category"), choices = CATEGORIES)
    details = models.CharField(max_length = 255, verbose_name = "Details", help_text = _("Enter the informations like total km, expense meal, etc."))
    justificatif = models.FileField(upload_to=user_directory_path, verbose_name = _("Justificatif"))

    def __str__(self):
        return self.date
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import Timesheet

class TimesheetForm(ModelForm):
    class Meta:
        model = Timesheet
        fields = ['date', 'title', 'working_hour']
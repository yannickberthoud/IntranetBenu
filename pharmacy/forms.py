from django.forms import ModelForm
from .models import Pharmacy
from employee.models import User

class PharmacyForm(ModelForm):
    class Meta:
       model = Pharmacy
       fields = ['name', 'email', 'phone', 'fax', 'manager', 'street', 'npa', 'city', 'canton']

    def __init__(self, *args, **kwargs):
       super(PharmacyForm, self).__init__(*args, **kwargs)
       self.fields['manager'].queryset = User.objects.filter(department = 'P', role = 'P')
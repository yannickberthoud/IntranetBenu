from django.contrib import admin

from .models import Pharmacy
from employee.models import User

class PharmacyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name','email', 'phone', 'fax')}),
        ('Employee', {'fields': ('manager',)}),
        ('Contact', {'fields': ('street', 'npa', 'city', 'canton')}),
    )

    def render_change_form(self, request, context, *args, **kwargs):
         context['adminform'].form.fields['manager'].queryset = User.objects.filter(department='P')
         return super(PharmacyAdmin, self).render_change_form(request, context, *args, **kwargs)

admin.site.register(Pharmacy, PharmacyAdmin)

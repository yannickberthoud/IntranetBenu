from django.contrib import admin

from .models import Timesheet, ExpanseReport

class ExpanseReportAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('owner',)}),
        ('expanse', {'fields': ('date', 'category', 'details', 'justificatif')})
    )

admin.site.register(ExpanseReport, ExpanseReportAdmin)

class TimesheetAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('owner',)}),
        ('timesheet', {'fields': ('date', 'working_hour',)}),
        ('work', {'fields': ('title',)})
    )

    list_display = ('week', 'date', 'owner', 'title',)

admin.site.register(Timesheet, TimesheetAdmin)

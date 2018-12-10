from django.contrib import admin

from .models import HelpDesk

class HelpDeskAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('client', 'priority', 'assigned_to')}),
        ('Bug', {'fields': ('category', 'description_of_the_problem', 'followed', 'solution')}),
        (None, {'fields': ('status',)})
    )

    search_fields = ['client', 'solution', 'description_of_the_problem']
    ordering = ['created_at', 'updated_at', 'priority']
    list_filter = ('status', 'priority', 'category', 'assigned_to')
    list_display = ('client', 'priority', 'assigned_to', 'created_at', 'updated_at', 'status')

admin.site.register(HelpDesk, HelpDeskAdmin)
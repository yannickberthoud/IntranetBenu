from django.contrib import admin

from .models import Improvement


class ImprovementAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('owner','module', 'title', 'description')}),
        ('Status', {'fields': ('is_approved', 'status', 'progress',)}),
        ('Advancement', {'fields': ('advancement',)})
    )

    list_display = ('title', 'description', 'is_approved', 'status', 'progress')

admin.site.register(Improvement, ImprovementAdmin)

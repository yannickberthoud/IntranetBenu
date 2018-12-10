from django.contrib import admin

from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Assignation', {'fields': ['department', 'assigned_to']}),
        ('Task', {'fields': ['priority', 'title', 'description', 'due_date', 'status']})
    )

    list_display = ('department', 'assigned_to', 'title', 'due_date', 'status')
    search_field = ('department', 'title', 'due_date')
    list_filter = ('department','status')

admin.site.register(Todo, TodoAdmin)

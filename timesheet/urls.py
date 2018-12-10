from django.urls import include, path, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView
from .models import Timesheet, ExpanseReport

from .views import index, details, timesheet_list, TimesheetDeleteView, TimesheetCreateView, TimesheetUpdateView, timesheet_total_per_month

urlpatterns = [
    path('', index, name='index'),
    #path(r'<int:pk>$', details, name='details'),
    path(r'new/', TimesheetCreateView.as_view(), name = 'new'),
    path(r'edit/<int:pk>/', TimesheetUpdateView.as_view(), name='edit'),
    path(r'delete/<int:pk>/', TimesheetDeleteView.as_view(), name='delete'),
    path('json-work/', timesheet_list, name = 'json-work'),
    path('json-month/', timesheet_total_per_month, name = 'json-month')
]
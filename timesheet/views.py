from rest_framework import status
from django.urls import reverse_lazy
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from .models import Timesheet
from .serializers import TimesheetSerializer
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.db.models import Sum, Count, Avg
from django.utils import timezone

from django.db import connection

import datetime
import time

class ReturnHour(object):
    def __init__(self, user, week):
        self.user = user
        self.week = week

    def get_week_hours(self):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT                
               SUM(working_hour)
            FROM
                timesheet_timesheet
            WHERE
                owner_id = %s
            AND
                week = %s
        """, [self.user, self.week])
        row = cursor.fetchone()[0]
        return str(row)

    def get_month_hours(self):
        last_year = timezone.now() - datetime.timedelta(days=365)  # for more accurate result, please use python-dateutil or similar tools
        return Timesheet.objects.annotate(total_hour=Sum('working_hour')).filter(owner=self.user, date__gte=last_year).order_by('date').values_list('working_hour', flat=True)

@login_required
def index(request):
    events_list = Timesheet.objects.filter(owner = request.user.pk, week = datetime.datetime.now().isocalendar()[1]).order_by('-working_hour')
    hours = ReturnHour(request.user.pk, datetime.datetime.now().isocalendar()[1])
    hours_week = hours.get_week_hours()

    return render(request, "timesheet/index.html", {'events_list': events_list, 'hours_week': hours_week})

class TimesheetCreateView(SuccessMessageMixin, CreateView):
    model = Timesheet
    template_name = 'timesheet/create.html'
    success_url = reverse_lazy('timesheet:index')
    success_message = "The event was successfully created."
    fields = ('owner', 'date', 'title', 'working_hour')

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )

class TimesheetUpdateView(SuccessMessageMixin, UpdateView):
    model = Timesheet
    template_name = 'timesheet/update.html'
    fields = ('owner', 'date', 'title', 'working_hour')
    success_url = reverse_lazy('timesheet:index')
    success_message = "The event was successfully updated."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )

class TimesheetDeleteView(SuccessMessageMixin, DeleteView):
    model = Timesheet
    success_url = reverse_lazy('timesheet:index')
    success_message = "The event was successfully deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TimesheetDeleteView, self).delete(request, *args, **kwargs)

@api_view(['GET', 'POST'])
def timesheet_list(request):
    if request.method == 'GET':
        timesheets = Timesheet.objects.filter(owner = request.user.pk, week = datetime.datetime.now().isocalendar()[1])
        serializer = TimesheetSerializer(timesheets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TimesheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def timesheet_total_per_month(request):
    hours = ReturnHour(request.user.pk, datetime.datetime.now().isocalendar()[1])
    timesheets = hours.get_month_hours()
    return Response({'data':timesheets})

@api_view(['GET', 'PUT', 'DELETE'])
def details(request, pk):
    """
    Retrieve, update or delete a timesheet instance.
    """
    try:
        timesheet = Timesheet.objects.get(pk=pk)
    except Timesheet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TimesheetSerializer(timesheet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TimesheetSerializer(timesheet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        print("delete method called.")
        timesheet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
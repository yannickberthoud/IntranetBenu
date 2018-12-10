from rest_framework import serializers
from employee.models import User
from .models import Timesheet
from django.utils.translation import ugettext_lazy as _

CATEGORIES = (
        ('C', _('Central work')),
        ('J', _('Justified absence')),
        ('T', _('Travel')),
        ('V', _('Vacation')),
    )

class TimesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timesheet
        fields ='__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Timesheet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.owner = validated_data.get('owner_id', instance.owner)
        instance.date = validated_data.get('date', instance.date)
        instance.title = validated_data.get('title', instance.title)
        instance.working_hour = validated_data.get('working_hour', instance.working_hour)
        return instance
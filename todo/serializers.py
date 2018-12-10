from rest_framework import serializers
from employee.models import User
from .models import Todo
from django.utils.translation import ugettext_lazy as _

CATEGORIES = (
        ('C', _('Central work')),
        ('J', _('Justified absence')),
        ('T', _('Travel')),
        ('V', _('Vacation')),
    )

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields ='__all__'
    # start = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    # end = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.department = validated_data.get('department', instance.department)
        instance.assigned_to = validated_data.get('assigned_to', instance.assigned_to)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.status = validated_data.get('status', instance.status)
        return instance
from rest_framework import status
from django.urls import reverse_lazy
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.db.models import F, Func

import datetime

@login_required
def index(request):
    todos_list = Todo.objects.filter(assigned_to = request.user.pk).order_by('priority', '-due_date', 'status')
    return render(request, "todo/index.html", {'todos_list': todos_list}) #,'total_hours_per_week': total_hours_per_week})

class TodoCreateView(SuccessMessageMixin, CreateView):
    model = Todo
    template_name = 'todo/create.html'
    success_url = reverse_lazy('todo:index')
    success_message = "The task was successfully created."
    fields = ('department', 'assigned_to', 'title', 'description', 'due_date', 'priority', 'status')

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )

class TodoDeleteView(SuccessMessageMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:index')
    success_message = "The task was successfully deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TodoDeleteView, self).delete(request, *args, **kwargs)

class TodoUpdateView(SuccessMessageMixin, UpdateView):
    model = Todo
    template_name = 'todo/update.html'
    fields = ('department', 'assigned_to', 'title', 'description', 'due_date', 'priority', 'status')
    success_url = reverse_lazy('todo:index')
    success_message = "The task was successfully updated."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )
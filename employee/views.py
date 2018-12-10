from rest_framework import status
from django.urls import reverse_lazy
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import FormView, DetailView

from .models import User

@login_required
def index(request):
    employees = User.objects.order_by('last_name', 'first_name', 'department', 'role')
    return render(request, 'employee/index.html', {'employees': employees})

class EmployeeDetailsView(DetailView):
    model = User
    template_name = 'employee/details.html'
    context_object_name = 'employee'

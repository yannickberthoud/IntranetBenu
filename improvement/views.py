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

from .models import Improvement

class ImprovementCreateView(SuccessMessageMixin,CreateView):
     model = Improvement
     fields = ['module', 'title', 'description']
     template_name = 'improvement/create.html'
     success_url=reverse_lazy('improvement:index')
     success_message = "The improvement was successfully created."

     def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ImprovementCreateView, self).form_valid(form)
     
     def get_success_message(self, cleaned_data):
         return self.success_message % dict(
             cleaned_data,
             title=self.object.title,
            )

class ImprovementDetailsView(DetailView):
    model = Improvement
    template_name = 'improvement/details.html'
    context_object_name = 'improvement'

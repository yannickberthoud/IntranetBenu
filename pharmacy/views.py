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

from .models import Pharmacy
from .forms import PharmacyForm
from employee.models import User

@login_required
def index(request):
    pharmacies = Pharmacy.objects.order_by('name', 'canton')
    return render(request, 'pharmacy/index.html', {'pharmacies': pharmacies})

class PharmacyDeleteView(DeleteView):
    model = Pharmacy
    success_url = reverse_lazy('pharmacy:index')
    success_message = "The pharmacy was successfully deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PharmacyDeleteView, self).delete(request, *args, **kwargs)

class PharmacyCreateView(SuccessMessageMixin, CreateView):
    model = Pharmacy
    template_name = 'pharmacy/create.html'
    success_url = reverse_lazy('pharmacy:index')
    success_message = "The pharmacy was successfully created."
    form_class = PharmacyForm

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )

class PharmacyDetailsView(DetailView):
    model = Pharmacy
    template_name = 'pharmacy/details.html'
    context_object_name = 'pharmacy'

class PharmacyUpdateView(SuccessMessageMixin, UpdateView):
    model = Pharmacy
    template_name = 'pharmacy/update.html'
    form_class = PharmacyForm
    success_url = reverse_lazy('pharmacy:index')
    success_message = "The pharmacy was successfully updated."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )
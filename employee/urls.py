from django.urls import include, path, reverse_lazy
from django.views.generic import ListView
from .models import User

from .views import index, EmployeeDetailsView#, PharmacyDeleteView, PharmacyCreateView, PharmacyUpdateView

urlpatterns = [
    path('', index, name='index'),
    path(r'details/<int:pk>/', EmployeeDetailsView.as_view(), name='details'),
]
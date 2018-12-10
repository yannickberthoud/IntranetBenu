from django.urls import include, path, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView
from .models import Pharmacy

from .views import index, PharmacyDeleteView, PharmacyCreateView, PharmacyUpdateView, PharmacyDetailsView

urlpatterns = [
    path('', index, name='index'),
    path(r'new/', PharmacyCreateView.as_view(), name = 'new'),
    path(r'details/<int:pk>/', PharmacyDetailsView.as_view(), name='details'),
    path(r'edit/<int:pk>/', PharmacyUpdateView.as_view(), name='edit'),
    path(r'delete/<int:pk>/', PharmacyDeleteView.as_view(), name='delete'),
]
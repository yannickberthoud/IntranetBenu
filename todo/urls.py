from django.urls import include, path, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView
from .models import Todo

from .views import index, TodoDeleteView, TodoCreateView, TodoUpdateView

urlpatterns = [
    path('', index, name='index'),
    path(r'new/', TodoCreateView.as_view(), name = 'new'),
    path(r'edit/<int:pk>/', TodoUpdateView.as_view(), name='edit'),
    path(r'delete/<int:pk>/', TodoDeleteView.as_view(), name='delete'),   
]
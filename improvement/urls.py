from django.urls import include, path, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.decorators import login_required

from .models import Improvement
from .views import ImprovementCreateView,ImprovementDetailsView

urlpatterns = [
    path('', login_required(ListView.as_view(
        model = Improvement,
        template_name = 'improvement/index.html',
        queryset = Improvement.objects.order_by('-created_at', 'updated_at', 'status', 'progress'),
        context_object_name = 'improvements_list'
    )), name='index'),
    path('new/', ImprovementCreateView.as_view(), name = 'new'),
    path('edit/<int:pk>', UpdateView.as_view(
        model = Improvement,
        fields = ['module', 'title', 'description'],
        template_name = 'improvement/create.html',
        success_url=reverse_lazy('improvement:index'),
    ), name = 'edit'),
    path(r'details/<int:pk>/', ImprovementDetailsView.as_view(), name='details'),

]
from django.urls import include, path, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.decorators import login_required
from .models import HelpDesk

urlpatterns = [
    path('', login_required(ListView.as_view(
        model = HelpDesk,
        template_name = 'support/helpdesk/index.html'
    )), name='index'),
    path('new/', CreateView.as_view(
        model = HelpDesk,
        fields = ['client', 'priority', 'assigned_to', 'category', 'description_of_the_problem', 'followed', 'solution', 'status'],
        template_name = 'support/helpdesk/create.html',
        success_url=reverse_lazy('support:index'),
    ), name = 'new'),
    path('edit/<int:pk>', UpdateView.as_view(
        model = HelpDesk,
        fields = ['client', 'priority', 'assigned_to', 'category', 'description_of_the_problem', 'followed', 'solution', 'status'],
        template_name = 'support/helpdesk/create.html',
        success_url=reverse_lazy('support:index'),
    ), name = 'edit'),

]
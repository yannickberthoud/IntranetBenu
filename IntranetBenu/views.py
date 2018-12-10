from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from employee.models import User

@login_required
def home(request):
    user = User.objects.get(pk=request.user.id)
    return render(request, 'IntranetBenu/index.html', {'user': user})
from django.shortcuts import render
from django.utils import timezone
from .models import *

# Create your views here.
def home(request):
    tasks = Task.objects.all()

    for task in tasks:
        if task.deadline:
            task.time_until_deadline = task.deadline - timezone.now()
            
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from todo.forms import TaskForm
from .models import Task
from django.contrib.auth.models import User

# Create your views here.
def tasks(request):
    if request.user.is_authenticated:
        user = request.user
        tasks = Task.objects.filter(user=user)

        for task in tasks:
            if task.deadline:
                task.time_until_deadline = task.deadline - timezone.now()
            
        return render(request, 'tasks/task_list.html', {'tasks': tasks})
    else:
        return render(request, 'tasks/task_list.html')
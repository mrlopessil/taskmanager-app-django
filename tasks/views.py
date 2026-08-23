from django.shortcuts import render, redirect
from django.utils import timezone

from todo.forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('tasks')
    
    return render(request, 'home.html')

@login_required
def tasks(request):
    user = request.user

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.save()

            return redirect('tasks')
    else:
        form = TaskForm()

    tasks = Task.objects.filter(user=user)
    
    for task in tasks:
        if task.deadline:
            task.time_until_deadline = task.deadline - timezone.now()
            
    context = {'form': form, 'tasks': tasks}

    return render(request, 'tasks/task_list.html', context)
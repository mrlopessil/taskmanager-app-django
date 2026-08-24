from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login
from django.utils import timezone

from todo.forms import TaskForm, CreateUserForm
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


def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('tasks')
    else:
        form = CreateUserForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def toggle_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(
            Task,
            id=task_id,
            user=request.user
        )
        task.done = not task.done
        task.save()

    return redirect('tasks')

from django import forms

from tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'priority']

        widgets = {
            'deadline': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                }
            ),
        }
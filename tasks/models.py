from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = 'low', 'Low Priority'
        MEDIUM = 'medium', 'Medium Priority'
        HIGH = 'high', 'High Priority'
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(
        max_length=32,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )

    def __str__(self):
        return self.title

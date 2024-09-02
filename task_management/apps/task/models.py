from django.db import models
from ..account.models import Account

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In progress'),
        ('completed', 'Completed'),
    ]
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=255, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Status")
    deadline = models.DateTimeField(verbose_name="Deadline Time")

    def __str__(self):
        return self.title
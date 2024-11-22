from django.db import models
from django.contrib.auth.models import User
from tasks .models import Task

class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name='tasks', on_delete=models.CASCADE)
    message = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=True)

    def __str__(self):
        return f'Notification for {self.user.username}'

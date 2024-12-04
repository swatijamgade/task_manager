from django.db import models
from django.contrib.auth.models import User

class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closes', 'Closed'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    assigned_to= models.ForeignKey(User, related_name='assigned_issues', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):

        return f"{self.title} ({self.status})"
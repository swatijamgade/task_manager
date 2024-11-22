from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    users = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name

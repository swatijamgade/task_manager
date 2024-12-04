from django.db import models
from django.contrib.auth.models import User
from issues.models import Issue
from django.core.exceptions import ValidationError

class Comment(models.Model):
    issue = models.ForeignKey(Issue, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.author.username} on Issue: {self.issue.title}"

    class Meta:
        ordering = ['-created_at']


    def clean(self):
        if not self.content.strip():
            raise ValidationError("comment content canot be empty")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def deactivate(self):
        self.is_active = False
        self.save()

    def reactivate(self):
        self.is_active = True
        self.save()


from django.db import models
from issues.models import Issue

class Comment(models.Model):
    issue = models.ForeignKey(Issue, related_name='comment', on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.issue.title}"

    @staticmethod
    def get_comment_by_user(user):
        return Comment.objects.filter(user=user)

    def update_comment(self, new_text):
        self.text = new_text
        self.save()
        return self
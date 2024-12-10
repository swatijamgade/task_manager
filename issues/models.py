from django.db import models




class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # Custom method to fetch all comments for an issue
    def get_Comment(self):
        return self.comments.all()

    # Custom method to add a comment to the issue
    def add_comment(self, user, text):
        return self.comments.create(user=user, text=text)


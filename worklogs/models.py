from django.db import models
from issues.models import Issue

class WorkLog(models.Model):
    issue = models.ForeignKey(Issue, related_name='work_logs', on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    hours_logged = models.FloatField()
    log_dated = models.DateTimeField()

    def __str__(self):
        return f"{self.hours_logged} hrs by {self.user} on {self.log_dated}"

    @classmethod
    def log_work(cls, issue, user, hours, log_date):
        return cls.objects.create(issue=issue, user=user, hours_logged=hours, log_date=log_date)

    @classmethod
    def logs_for_user_and_issue(cls, issue, user):
        return cls.objects.filter(issue=issue, user=user)
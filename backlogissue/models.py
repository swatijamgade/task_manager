from django.db import models
import csv
from django.core.files.base import ContentFile

class BacklogIssue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # Class method to bulk upload issues from CSV
    @classmethod
    def upload_csv(cls, file):
        issues = []
        reader = csv.reader(file.read().decode('utf-8').splitlines())
        for row in reader:
            title, description = row
            issues.append(cls(title=title, description=description))
        cls.objects.bulk_create(issues)
        return len(issues)

    # Class method to export backlog issues to a CSV file
    @classmethod
    def download_csv(cls):
        rows = cls.objects.values_list('title', 'description')
        csv_data = "\n".join([",".join(map(str, row)) for row in rows])
        return ContentFile(csv_data, name="backlog.csv")
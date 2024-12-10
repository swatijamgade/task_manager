from rest_framework import serializers
from .models import BacklogIssue

class BlackLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BacklogIssue
        fields = '__all__'
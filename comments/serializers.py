from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'issue', 'user', 'text', 'created_at']
        read_only_fields = ['id', 'created_at']

from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    issue = serializers.StringRelatedField(read_only=True)


    class Meta:
        models = Comment
        fields = ['id', 'issue', 'author', 'content', 'created_at', 'updated_at', 'is_active']

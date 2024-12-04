from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied

# Create, read, update, and delete (CRUD) operations for comments.
# Custom actions for deactivating and reactivating comments.
# Permissions to ensure users can only modify their own comments.

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


    def get_queryset(self):
        """Filter comments by task"""
        issue_id = self.kwargs.get('issue_id')
        if issue_id:
            return Comment.objects.filter(issue_id=issue_id, is_active=True)
        return Comment.objects.filter(is_active=True)

    def perform_create(self, serializer):
        """Override to set the author to the current user"""
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """Override update method to ensure users can only update their own comments"""
        comment = self.get_object()
        if comment.author != self.request.user:
            raise PermissionDenied("You cannot edit someone else's comment.")
        serializer.save()

    def perform_destroy(self, instance):
        """Override destroy method to ensure users can only delete their own comments"""
        if instance.author !=self.request._user:
            raise PermissionDenied("You cannot delete someone else's comment.")
        instance.delete()

    @action(detail=True, method=['post'])
    def deactivate(self, request, pk=None):

        comment = self.get_object()
        if comment.author != request.user:
            raise PermissionDenied("You cannot deactivate someone else's comment.")
        comment.deactivate()
        return Response({'status': 'comment deactivated'})

    @action(detail=True, method=['post'])
    def reactivate(self, request, pk=None):
        comment = self.get_object()
        if comment.author != request.user:
            raise PermissionDenied("You cannot reactivate someone else's comment.")
        comment.reactivate()
        return Response({'status': 'comment reactivated'})


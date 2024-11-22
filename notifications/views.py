from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Notification
from .serializers import NotificationSerializer

class NotificationAPIView(APIView):


    def get(self, request):
        notifications = Notification.objects.filter(user=request.user)
        if not notifications.exists():
            return Response({'detail: No notifications found for this user.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

class NotificationDetailAPIView(APIView):

    def put(self, request, pk):
        notification = get_object_or_404(Notification, pk=pk, user=request.user)
        serializer = NotificationSerializer(notification, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail: Notification updated successfully.','data: serializer.data' }, status=status.HTTP_200_OK)
        return Response({ 'detail: "Failed to update notification.''errors: serializer.errors' }, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        notification = get_object_or_404(Notification, pk=pk, user=request.user)
        notification.delete()
        return Response({ "detail": f"Notification with ID {pk} deleted successfully." }, status=status.HTTP_204_NO_CONTENT)

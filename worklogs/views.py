from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WorkLog
from .serializers import WorkLogSerializer

class WorkLogListCreateAPIView(APIView):
    """
    API to list all work logs for a specific issue or create a new work log.
    """

    def get(self, request, issue_id):
        """
        Retrieve all work logs for a specific issue.
        """
        logs = WorkLog.objects.filter(issue_id=issue_id)
        serializer = WorkLogSerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request, issue_id):
        """
        Create a new work log for a specific issue.
        """
        data = request.data
        data['issue'] = issue_id  # Assign the issue ID from the URL
        serializer = WorkLogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkLogDetailAPIView(APIView):
    """
    API to retrieve, update, or delete a specific work log.
    """

    def get(self, request, pk):
        """
        Retrieve a specific work log by ID.
        """
        try:
            log = WorkLog.objects.get(pk=pk)
        except WorkLog.DoesNotExist:
            return Response({"error": "Work log not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = WorkLogSerializer(log)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a specific work log.
        """
        try:
            log = WorkLog.objects.get(pk=pk)
        except WorkLog.DoesNotExist:
            return Response({"error": "Work log not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = WorkLogSerializer(log, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific work log.
        """
        try:
            log = WorkLog.objects.get(pk=pk)
        except WorkLog.DoesNotExist:
            return Response({"error": "Work log not found"}, status=status.HTTP_404_NOT_FOUND)

        log.delete()
        return Response({"message": "Work log deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

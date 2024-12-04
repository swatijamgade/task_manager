from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Issue
from .serializers import IssueSerializer
from django.contrib.auth.models import User

class IssueCreateView(APIView):

    def post(self, request):
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message : Issue created successfully', 'data : serializer.data'}, status=status.HTTP_201_CREATED)
        return Response({'message: Error creating issue', 'errors : serializer.errors'}, status=status.HTTP_400_BAD_REQUEST)

class IssueListView(APIView):

    def get(self, request):
        issues = Issue.objects.all()  # Retrieve all issues from the database
        serializer = IssueSerializer(issues, many=True)
        return Response({'message : Issues retrieved successfully.', 'data : serializer.data'}, status=status.HTTP_200_OK)


class IssueDeatilView(APIView):

    def get(self, request, pk):
        try:
            issue = Issue.objects.get(pk=pk)
        except Issue.DoesNotExit:
            return Response({'message : Issue not found.', 'error : Issue does not exit'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message : Issue details retrieved successfully.','data : serializer.data'}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            issue = Issue.objects.get(pk=pk)
        except Issue.DoesNotExit:
            return Response({'message : Issue not found.', 'error : The issue does not exit'}, status=status.HTTP_404_NOT_FOUND)

        serializer = IssueSerializer(issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message : Issue updated successfully', 'data : serializer.data'}, status=status.HTTP_200_OK)
        return Response({' message : Error updating issue', 'data : serializer.data'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            issue = Issue.objects.get(pk=pk)
        except Issue.DoesNotExit:
            return Response({'message : Issue not found', 'error : Issue trying to delete does not exit'}, staus=status.HTTP_404_NOT_FOUND)
        issue.delete()
        return Response({'message : Issue deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import BacklogIssue
from .serializers import BlackLogSerializer


class BackLogIssueListCreateAPIView(APIView):
    """
       API to list and create BackLogIssues.
       """
    def get(self, request):
        issue = BacklogIssue.objects.all()
        serializer = BlackLogSerializer(issue, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlackLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message : Backlogissue created'}, status=status.HTTP_201_CREATED)
        return Response({'error : Error'}, status=status.HTTP_400_BAD_REQUEST)

class BackLogIssueUploadCSVAPIView(APIView):
    """
       API to upload CSV file to create BackLogIssues.
       """

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error : "No file provided'}, status=status.HTTP_400_BAD_REQUEST)
        created_count = BacklogIssue.upload_csv(file)
        return Response({"message": f"{created_count} issues uploaded successfully"})

class BackLogIssueDownloadCSVAPIView(APIView):
    """
       API to download all BackLogIssues as a CSV file.
       """

    def get(self, request):
        csv_file = BacklogIssue.download_csv()
        response = HttpResponse(csv_file, content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'
        return response



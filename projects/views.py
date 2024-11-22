
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # Make sure this is imported
from .models import Project
from .serializers import ProjectSerializer


class ProjectListView(APIView):

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response({ 'detail': 'Projects retrieved successfully.','data': serializer.data
        })

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Project created successfully.','data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'detail': 'Project creation failed.','errors': serializer.errors }, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailView(APIView):

    def get(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExit:
            return Response({'detail: Project not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectSerializer(project)
        return Response({'detail : Project retrive succesfully'}, 'data: serializer.data')

    def put(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
        except project.DoesNotExit:
            return Response({'detail : Project not found'})

        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail : Project updated succeesfully'}, status=status.HTTP_201_CREATED)
        return Response({'detail : Project update failed', 'error: serializer.error'}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request, pk):
        try:
            project = Project.objects.all()
        except Project.DoesNotExit:
            return Response({'detail : Project not found'}, status=status.HTTP_404_NOT_FOUND)
        project.delete()
        return Response({'detail : Project deleteed succesfully'}, status=status.HTTP_204_NO_CONTENT)

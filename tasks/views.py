from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer


class TaskListView(APIView):

    def get(self, request):
        tasks = Task.objects.filter(assigned_to=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response({'detail': 'Tasks assigned successfully.','data': serializer.data })

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(assigned_to=request.user)
            return Response({'detail': 'Task successfully created.','data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'detail': 'Task creation failed.','errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):

    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({'detail': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task)
        return Response({ 'detail': 'Task retrieved successfully.','data': serializer.data})

    def put(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({'detail': 'Task not found.' }, status=status.HTTP_404_NOT_FOUND)


        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Task updated successfully.','data': serializer.data})
        return Response({'detail': 'Task update failed.','errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({'detail': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({'detail': 'Task deleted successfully.' }, status=status.HTTP_204_NO_CONTENT)

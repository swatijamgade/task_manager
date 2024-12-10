from django.urls import path
from .views import WorkLogListCreateAPIView, WorkLogDetailAPIView

urlpatterns = [

    path('worklogs/<int:issue_id>/', WorkLogListCreateAPIView.as_view(), name='worklogs-list-create'),

    path('worklogs/<int:pk>/', WorkLogDetailAPIView.as_view(), name='worklogs-detail'),
]
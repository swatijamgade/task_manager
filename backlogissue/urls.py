from django.urls import path
from .views import BackLogIssueListCreateAPIView, BackLogIssueUploadCSVAPIView, BackLogIssueDownloadCSVAPIView

urlpatterns = [

    path('backlog/', BackLogIssueListCreateAPIView.as_view(), name='backlog-list-create'),
    path('backlog/upload/', BackLogIssueUploadCSVAPIView.as_view(), name='backlog-upload'),
    path('backlog/download/', BackLogIssueDownloadCSVAPIView.as_view(), name='backlog-download'),
]
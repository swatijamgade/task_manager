from django.urls import path
from .views import IssueCreateView, IssueListView, IssueDeatilView


urlpatterns = [

    path('issues/', IssueCreateView.as_view(), name='issue-list'),
    path('issues/create/', IssueCreateView.as_view(), name='issue-create'),
    path('issues/<int:pk/', IssueDeatilView.as_view(), name='issue-detail'),
]
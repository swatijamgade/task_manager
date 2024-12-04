from django.urls import path
from . import views

urlpatterns = [

    path('comments/', views.CommentViewSet.as_view({'get': 'list'}), name='comment-list'),
    path('comments/', views.CommentViewSet.as_view({'post': 'create'}), name='comment-create'),
    path('comments/<int:id>/', views.CommentViewSet.as_view({'get': 'retrieve'}), name='comment-retrieve'),
    path('comments/<int:id>/', views.CommentViewSet.as_view({'put': 'update', 'patch': 'update'}),name='comment-update'),
    path('comments/<int:id>/', views.CommentViewSet.as_view({'delete': 'destroy'}), name='comment-destroy'),
    path('comments/<int:id>/deactivate/', views.CommentViewSet.as_view({'post': 'deactivate'}), name='comment-deactivate'),
    path('comments/<int:id>/reactivate/', views.CommentViewSet.as_view({'post': 'reactivate'}),name='comment-reactivate'),
]

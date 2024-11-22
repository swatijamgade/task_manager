from django.urls import path
from .views import NotificationAPIView, NotificationDetailAPIView

urlpatterns = [

    path('notifications/', NotificationAPIView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', NotificationDetailAPIView.as_view(), name='notification-detail'),

]

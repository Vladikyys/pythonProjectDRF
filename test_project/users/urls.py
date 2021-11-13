from django.urls import path

from .views import UserListCreateView, UserDetailView, AnnouncementView, AnnouncementExecutorView

urlpatterns = [
    # gets all user and create a new
    path('all-users/', UserListCreateView.as_view(), name='all-users'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user'),
    path('announcements/', AnnouncementView.as_view(), name='announcements'),
    path('announcements/executor/', AnnouncementExecutorView.as_view(), name='announcements-executor'),
]

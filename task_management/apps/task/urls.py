
from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.TaskListApiView.as_view(), name="list"),
    path("detail/<int:pk>/", views.TaskDetailOrDeleteApiView.as_view(), name = "detail"),
    path('create/', views.TaskCreateApiView.as_view(), name="create_task"),
    path('edit/<int:pk>/', views.TaskStatusUpdateApiView.as_view(), name="edit_status")
]
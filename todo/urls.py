from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/add/', views.TaskCreateView.as_view(), name='add_task'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='update_task'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete_task'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),

    path('tasks/<int:pk>/toggle/', views.ToggleTaskStatusView.as_view(), name='toggle_task_status'),
    path('tasks/<int:pk>/add_user/', views.AddTaskUserView.as_view(), name='add_task_user'),
    path('tasks/<int:pk>/remove_user/', views.RemoveTaskUserView.as_view(), name='remove_task_user'),

    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('tags/add/', views.TagCreateView.as_view(), name='add_tag'),
    path('tags/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('tags/<int:pk>/delete/', views.TagDeleteView.as_view(), name='delete_tag'),
    path('tags/<int:pk>/update/', views.TagUpdateView.as_view(), name='update_tag'),
]


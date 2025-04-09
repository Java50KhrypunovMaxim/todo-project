from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/add/', views.TaskCreateView.as_view(), name='add_task'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='update_task'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete_task'),
    path('tasks/<int:task_id>/toggle/', views.toggle_task_status, name='toggle_task_status'),
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('tags/add/', views.TagCreateView.as_view(), name='add_tag'),
    path('tags/<int:pk>/delete/', views.TagDeleteView.as_view(), name='delete_tag'),
]
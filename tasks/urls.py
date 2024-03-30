from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.TaskListView.as_view(), name='tasks_list'),
    path('tasks_list/<int:id>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('create_task/', views.TaskCreateView.as_view(), name='create_task'),
    path('tasks_list/<int:id>/update/', views.TaskUpdateView.as_view(), name='update_task'),
    path('tasks_list/<int:id>/delete/', views.TaskDeleteView.as_view(), name='delete_task'),
    path('search/', views.SearchTaskView.as_view(), name='search'),
]

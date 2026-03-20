from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todolist'),
    path('delete/<int:task_id>/', views.delete_task, name='delete'),
]
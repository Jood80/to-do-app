from django.urls import path
from . import views


urlpatterns = [
    path('', views.toDo, name='list'),
    path('update/<str:PK>/', views.updateTask, name='updated_task'),
    path('delete/<str:PK>/', views.deleteTask, name='deleted_task'),
]

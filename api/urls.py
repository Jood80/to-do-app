from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.main, name='main'),
    path('todo', views.toDo, name='list'),

]

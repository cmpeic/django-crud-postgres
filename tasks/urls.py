from django.urls import path
from .views import lista_tareas,create_task,delete_task

urlpatterns = [
    path('',lista_tareas),
    path('new/',create_task, name= 'create_task'),
    path('delete_task/<int:tarea_id>/',delete_task, name= 'delete_task'),
    
]
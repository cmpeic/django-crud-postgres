from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def lista_tareas(request):
    tasks_l = Task.objects.all()
    print(tasks_l)
    return render(request,'lista_tareas.html', {"tasks_p" : tasks_l})

# Guardar datos
def create_task(request):
    print(request.POST['description'])
    task = Task(title = request.POST['title'], description = request.POST['description'])
    task.save()
    return redirect('/tasks/')

def delete_task(request, tarea_id):
    print(tarea_id)
    task = Task.objects.get(id=tarea_id)
    task.delete()
    return redirect('/tasks/')
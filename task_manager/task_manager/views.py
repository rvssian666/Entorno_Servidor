from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import redirect,get_object_or_404

def get_all_list(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            new_list = TaskList(name=name)
            new_list.save()
            return redirect('all_list') 

    # Esto se ejecuta en el GET o después del redirect
    all_list = TaskList.objects.all()
    return render(request, 'index.html', {'all_list': all_list})


def get_list(request,id):
    all_list=TaskList.objects.get(id=id)
    return render(request,'index.html',{'all_list':all_list})

# Eliminar  de tareas
def delete_task_list(request,list_id):
 list=get_object_or_404(TaskList,id=list_id)
 list.delete()
 return redirect('all_list')

# Obtener tareas de una lista
def get_task(request, list_id):
    task_list = get_object_or_404(TaskList, id=list_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            new_task = Task(title=title)
            new_task.save()
            return redirect('get_task', lista_id=list_id)  
    tasks = task_list.task_set.all()
    return render(request, 'task.html', {
        'tasks': tasks, 
        'task_list': task_list
    })

   



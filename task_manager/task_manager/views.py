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
    all_list = TaskList.objects.all()
    return render(request, 'index.html', {'all_list': all_list})


def get_list(request,id):
    all_list=TaskList.objects.get(id=id)
    return render(request,'index.html',{'all_list':all_list})

# Eliminar lista tareas
def delete_task_list(request,list_id):
 list=get_object_or_404(TaskList,id=list_id)
 list.delete()
 return redirect('all_list')


def get_task(request, lista_id):
    task_list = get_object_or_404(TaskList, id=lista_id)
    
    # Si el usuario envía el formulario (POST)
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title, task_list=task_list)
            return redirect('get_task', lista_id=lista_id)

    # Si el usuario solo entra a ver (GET)
    tasks = task_list.task_set.all() 
    context={
        'tasks':tasks,
        'task_list':task_list
    }
    return render(request, 'task.html', context)



def delete_especific_task(request,task_id,lista_id):
 task=get_object_or_404(Task,id=task_id)
 id_deleted=task.task_list.id
 task.delete()
 return redirect('get_task',lista_id=id_deleted)



from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskList
from django.shortcuts import redirect

###Queda preguntar si es mejor separar la creacion de listas de la obtencion
''''
Es decir hacer funciones para el CRUD ,  '''
def get_all_list(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            new_list = TaskList(name=name)
            new_list.save()
            # En lugar de HttpResponse, usamos redirect
            # Esto recarga la página 'all_lists' (la que definiste en urls.py)
            return redirect('all_list') 

    # Esto se ejecuta en el GET o después del redirect
    all_list = TaskList.objects.all()
    return render(request, 'index.html', {'all_list': all_list})


def get_list(request,id):
    all_list=TaskList.objects.get(id=id)
    return render(request,'index.html',{'all_list':all_list})

    
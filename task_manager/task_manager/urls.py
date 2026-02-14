
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.get_all_list,name='all_list'),
    path('lists/',views.get_all_list,name='all_list'),
    path('lists/<list_id>/',views.delete_task_list,name='delete_task_list'),
    #para obtener o pinchar una tarea específica
    path('lists/<int:lista_id>/tasks/', views.get_task, name='get_task'),
    path('lists/<int:lista_id>/tasks/<int:task_id>/', views.delete_especific_task, name='delete_especific_task'),
    
    
]

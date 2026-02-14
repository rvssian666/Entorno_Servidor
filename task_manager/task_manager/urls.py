
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # aqui pongo la url para la vista de tareas,
    path('',views.get_all_list,name='all_list'),
    path('lists/',views.get_all_list,name='all_list'),
    path('lists/<list_id>/',views.delete_task_list,name='delete_task_list'),
]

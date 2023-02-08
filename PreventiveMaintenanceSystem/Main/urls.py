from django.urls import path, include
from . import views
from .views import TaskList, MachineList, total_maquinas, total_tarefas, total_concluidas, total_pendentes, cadastro_maquina, cadastro_tarefa
from .views import altera_status, altera_statusP, machinedata, machinedatalist, cadastroperfil, home

urlpatterns = [


path('total_maquinas', total_maquinas, name='total_maquinas'),
path('total_concluidas', total_concluidas, name='total_concluidas'),
path('total_pendentes', total_pendentes, name='total_pendentes'),
path('total_tarefas', total_tarefas, name='total_tarefas'),

path('cadastro_maquina', views.cadastro_maquina, name='cadastro_maquina'),
path('cadastro_tarefa', views.cadastro_tarefa, name='cadastro_tarefa'),
path('', views.MachineList, name=''),
path('machinedatalist', views.machinedatalist, name='machinedatalist'),
path('cadastroperfil', views.cadastroperfil, name='cadastroperfil'),

path('TaskList/<int:maquina_id>', views.TaskList, name='TaskList'),
path('MachineListP', views.MachineListP, name='MachineListP'),
path('MachineListC', views.MachineListC, name='MachineListC'),
path('machinedata/<int:maquina_id>/', views.machinedata, name='machinedata'),
path('home', views.home, name='home'),

path('altera_status/<int:id>/<int:item_id>', views.altera_status, name='altera_status'),
path('altera_statusP/<int:id>/<int:item_id>', views.altera_statusP, name='altera_statusP'),

]
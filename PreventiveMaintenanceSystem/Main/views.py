from django.shortcuts import render
from .models import maquina, tarefa, Perfil
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.db.models import Count
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import MaquinaForm, TarefaForm, cadastroperfilform
import datetime 
from datetime import datetime, date, timedelta
from django.views.generic import ListView
### altera status ###

def altera_status(request, id):
    tarefas = tarefa.objects.get(id=id)
    tarefas.status = 'Concluida'
    tarefas.save()

    return redirect('')


def reset_tarefas():
    tarefas_agendadas = tarefa.objects.all()
    for tarefas in tarefas_agendadas:
        tarefas.item.refresh_from_db()
        if tarefas.item.prazo <= datetime.now().date():
            if tarefas.status == 'Concluida':
                tarefas.status = 'Agendado'
                tarefas.save()
            elif tarefas.status == 'Agendado':
                tarefas.status = 'Pendente'
                tarefas.save()

def resettime():
    tarefas_agendadas = tarefa.objects.all()
    for tarefas in tarefas_agendadas:
        if tarefas.item.prazo <= datetime.now().date():
            tarefas.item.prazo = date.today() + timedelta(days=tarefas.item.periodicidade)
            tarefas.item.save()                
                
def altera_status(request, id, item_id):
    tarefas = tarefa.objects.get(id=id)
    tarefas.status = 'Concluida'
    tarefas.save()
    return redirect('TaskList', item_id)

def altera_statusP(request, id, item_id):
    tarefas = tarefa.objects.get(id=id)
    tarefas.status = 'Pendente'
    tarefas.save()
    return redirect('TaskList', item_id)

###  lista ###
def home(request):
    Maquina = maquina.objects.all()
    tarefas = tarefa.objects.exclude(status='Concluida').order_by('item__prazo')
    
    
    return render(request, 'home.html', {'tarefas': tarefas})

def TaskList(request, maquina_id, *args):
    Maquina = get_object_or_404(maquina, pk=maquina_id)
    tarefas = tarefa.objects.filter(item_id=maquina_id).order_by('nome')
    return render(request, 'Tasklist.html', {'tarefas': tarefas, 'maquina':Maquina})

def MachineList(request):
    reset_tarefas()
    resettime()
    maquinas = maquina.objects.annotate(
        num_subtarefas_total=Count('tarefa'),
        num_subtarefas_concluidas=Count('tarefa', filter=Q(tarefa__status='concluida')),
        num_subtarefas_agendadas=Count('tarefa', filter=Q(tarefa__status='Agendado')),
        num_subtarefas_pendentes=Count('tarefa', filter=Q(tarefa__status='pendente'))
    ).order_by('nome')
    return render(request, 'MachineList.html', {'maquinas': maquinas})

def totaisC(request):
    totais = maquina.objects.annotate(
        num_total=Count('tarefa'),
        num_concluidas=Count('tarefa', filter=Q(tarefa__status='concluida')),
        num_pendentes=Count('tarefa', filter=Q(tarefa__status='pendente'))
    )
    return render(request, 'MachineListC.html', {'totais': totais})

def MachineListP(request):
    maquinas = maquina.objects.filter(tarefa__status='Pendente').annotate(
        num_subtarefas_pendentes=Count('tarefa', filter=Q(tarefa__status='Pendente'))
    ).order_by('nome')
    return render(request, 'MachineListP.html', {'maquinas': maquinas})
    
def MachineListC(request):
    maquinas = maquina.objects.filter(~Q(tarefa__status='pendente')).annotate(
        num_tarefas_concluidas=Count('tarefa', filter=Q(tarefa__status='Concluida'))
            ).order_by('nome')
    return render(request, 'MachineListC.html', {'maquinas': maquinas})

###  cadastro  ###

def cadastro_maquina(request):
    form = MaquinaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cadastro_tarefa')
    return render(request, 'cadastroMaquinas.html', {'form': form})

def cadastroperfil(request):
    if request.method == 'POST':
        form = cadastroperfilform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('machinedatalist')
    else:
        form = cadastroperfilform()
    return render(request, 'cadastroperfil.html', {'form': form})
    
def cadastro_tarefa(request):
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('')
    return render(request, 'cadastroTarefas.html', {'form': form})

### total json results ###

def total_maquinas(request):
    total = maquina.objects.count()
    return JsonResponse(total, safe=False)

def total_tarefas(request):
    total = tarefa.objects.count()
    return JsonResponse(total, safe=False)

def total_concluidas(request):
    total = tarefa.objects.filter(status='Concluida').count()
    return JsonResponse(total, safe=False)

def total_pendentes(request):
    total = tarefa.objects.filter(status='Pendente').count()
    return JsonResponse(total, safe=False)


### perfil ###

def machinedata(request, maquina_id):
    maquina = Perfil.objects.get(id=maquina_id)
    return render(request, 'machinedata.html', {'maquina': maquina})


def machinedatalist(request):
    perfis = Perfil.objects.annotate()
    return render(request, 'machinedatalist.html', {'perfis': perfis})

def machinedata(request, maquina_id):
    try:
        maquina = Perfil.objects.get(id=maquina_id)
    except Perfil.DoesNotExist:
        return redirect('cadastroperfil')
    return render(request, 'machinedata.html', {'maquina': maquina})



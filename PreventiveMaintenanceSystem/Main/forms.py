from django import forms
from .models import maquina, tarefa, Perfil

class MaquinaForm(forms.ModelForm):
    class Meta:
        model = maquina
        fields = ['nome', 'periodicidade']
        
class cadastroperfilform(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['Referencia', 'Nome', 'Informações', 'Foto']

class TarefaForm(forms.ModelForm):
    class Meta:
        model = tarefa
        fields = ['item', 'nome', 'status']
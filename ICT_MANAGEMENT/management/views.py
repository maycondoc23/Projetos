from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .forms import  usuarioform,edituserprofile,ideapad31ict3form, ideapad3aict3form, ideapad3iict3form, e14ict3form, n50sict3form, m75ict3form,ideapad3aict1form, ideapad3iict1form, n50sict1form, m75ict1form, e14ict1form, ideapad31ict1form,n50sict2form, n50sict2form,m75ict2form, ideapad31ict2form, ideapad3aict2form, ideapad3iict2form, ideapad31ict2, ideapad3aict2, ideapad3iict2, e14ict2form
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import coberturatotalN50s, coberturatotalm75, coberturatotal3a, coberturatotal3i,coberturatotale14,coberturatotalideapad1, n50sict1, n50sict2,n50sict3,ideapad31ict1,ideapad31ict2,ideapad31ict3,ideapad3aict1,ideapad3aict2,ideapad3aict3,ideapad3iict1,ideapad3iict2,ideapad3iict3,e14ict1,e14ict2,e14ict3,m75ict1,m75ict2,m75ict3
from django.http import JsonResponse
from datetime import datetime
from django.shortcuts import render
from datetime import datetime
import mysql.connector
from django.views import generic
from mysql.connector import Error

def conectar():
    try:
        global conexao
        conexao = mysql.connector.connect(host='127.0.0.1', database='ictmanagement', password='1234', user='host')
        
    except Error as erro:
        print('erro de conexão')

def atualizar(comando):
    cursor = conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()

@login_required
def home(request):
    return render(request, 'management/home.html')

def index(request):
    myDate = datetime.now()
    return render(request, 'management/index.html', {
        'myDate': myDate
    })

class PaginaInicial(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('home')
    template_name = 'management/home.html'


#ict1
@login_required
def ict1statusneo(request):
    if request.method == "GET":
         form = n50sict1form()
         context = {
            'form': form
         }
         return render(request, 'management/ICT1FORM/ict1statusneo.html', context=context)
    else:
        form = n50sict1form(request.POST)
        if form.is_valid():
            
            conectar()
            sttstest = form.save()
            form = n50sict1form
            
        context = {
            'form': form
         }
        return render(request, 'management/ICT1FORM/ict1statusneo.html', context=context)

@login_required
def ict1statusm75(request):
    if request.method == "GET":
         form = m75ict1form()
         context = {
            'form': form
         }
         return render(request, 'management/ICT1FORM/ict1statusm75.html', context=context)
    else:
        form = m75ict1form(request.POST)
        if form.is_valid():
            conectar()
            sttstest = form.save()
            form = m75ict1form
        context = {
            'form': form
         }
        return render(request, 'management/ICT1FORM/ict1statusm75.html', context=context)

@login_required
def ict1statusideapad3i(request):
    if request.method == "GET":
         form = ideapad3iict1form()
         context = {
            'form': form
         }
         return render(request, 'management/ICT1FORM/ict1statusideapad3i.html', context=context)
    else:
        form = ideapad3iict1form(request.POST)
        if form.is_valid():
            conectar()
            sttstest = form.save()
            form = ideapad3iict1form
        context = {
            'form': form
         }
        return render(request, 'management/ICT1FORM/ict1statusideapad3i.html', context=context)

@login_required
def ict1statusideapad3a(request):
    if request.method == "GET":
         form = ideapad3aict1form()
         context = {
            'form': form
         }
         return render(request, 'management/ICT1FORM/ict1statusideapad3a.html', context=context)
    else:
        form = ideapad3aict1form(request.POST)
        if form.is_valid():
            conectar()
            sttstest = form.save()
            form = ideapad3aict1form
        context = {
            'form': form
         }
        return render(request, 'management/ICT1FORM/ict1statusideapad3a.html', context=context)

@login_required
def ict1statuse14(request):
    if request.method == "GET":
         form = e14ict1form()
         context = {
            'form': form
         }
         return render(request, 'management/ICT1FORM/ict1statuse14.html', context=context)
    else:
        form = e14ict1form(request.POST)
        if form.is_valid():
            conectar()
            sttstest = form.save()
            form = e14ict1form
        context = {
            'form': form
         }
        return render(request, 'management/ICT1FORM/ict1statuse14.html', context=context)

@login_required
def ict1statusideapad1(request):
    if request.method == "GET":
         form = ideapad31ict1form()
         context = {
            'form': form
         }
         return render(request, 'management/ICT1FORM/ict1statusideapad1.html', context=context)
    else:
        form = ideapad31ict1form(request.POST)
        if form.is_valid():
            conectar()
            sttstest = form.save()
            form = ideapad31ict1form
        context = {
            'form': form
         }
        return render(request, 'management/ICT1FORM/ict1statusideapad1.html', context=context)



#ict2
@login_required
def ict2statusneo(request):
    if request.method == "GET":
        form = n50sict2form()
        context = {
           'form': form
        }
        return render(request, 'management/ICT2FORM/ict2statusneo.html', context=context)
    else:
        form = n50sict2form(request.POST)
        if form.is_valid():
            comando = 'UPDATE ictmanagement.management_coberturatotaln50s SET tested = tested-1 WHERE Id = 1'
            conectar()
            sttstest = form.save()
            form = n50sict2form
        context = {
            'form': form
        }
        return render(atualizar(comando),  'management/ICT2FORM/ict2statusneo.html', context=context)

@login_required
def ict2statusm75(request):
    if request.method == "GET":
         form = m75ict2form()
         context = {
            'form': form
         }
         return render(request, 'management/ICT2FORM/ict2statusm75.html', context=context)
    else:
        form = m75ict2form(request.POST)
        if form.is_valid():
            comando = 'UPDATE ictmanagement.management_coberturatotalm75 SET tested = tested-1 WHERE Id = 1'
            conectar()
            sttstest = form.save()
            form = m75ict2form
        context = {
            'form': form
         }
        return render(atualizar(comando), 'management/ICT2FORM/ict2statusm75.html', context=context)

@login_required
def ict2statusideapad3i(request):
    if request.method == "GET":
         form = ideapad3iict2form()
         context = {
            'form': form
         }
         return render(request, 'management/ICT2FORM/ict2statusideapad3i.html', context=context)
    else:
        form = ideapad3iict2form(request.POST)
        if form.is_valid():
            conectar()
            sttstest = form.save()
            form = ideapad3iict2form
        context = {
            'form': form
         }
        return render(request, 'management/ICT2FORM/ict2statusideapad3i.html', context=context)

@login_required
def ict2statusideapad3a(request):
    if request.method == "GET":
         form = ideapad3aict2form()
         context = {
            'form': form
         }
         return render(request, 'management/ICT2FORM/ict2statusideapad3a.html', context=context)
    else:
        form = ideapad3aict2form(request.POST)
        if form.is_valid():
            conectar()
            sttstest = form.save()
            form = ideapad3aict2form
        context = {
            'form': form
         }
        return render(request, 'management/ICT2FORM/ict2statusideapad3a.html', context=context)

@login_required
def ict2statuse14(request):
    if request.method == "GET":
         form = e14ict2form()
         context = {
            'form': form
         }
         return render(request, 'management/ICT2FORM/ict2statuse14.html', context=context)
    else:
        form = e14ict2form(request.POST)
        if form.is_valid():
            conectar()
            sttstest = form.save()
            form = e14ict2form
        context = {
            'form': form
         }
        return render(request, 'management/ICT2FORM/ict2statuse14.html', context=context)

@login_required
def ict2statusideapad1(request):
    if request.method == "GET":
         form = ideapad31ict2form()
         context = {
            'form': form
         }
         return render(request, 'management/ICT2FORM/ict2statusideapad1.html', context=context)
    else:
        form = ideapad31ict2form(request.POST)
        if form.is_valid():
            conectar()
            sttstest = form.save()
            form = ideapad31ict2form
        context = {
            'form': form
         }
        return render(request, 'management/ICT2FORM/ict2statusideapad1.html', context=context)


#ict3
@login_required
def ict3statusneo(request):
    if request.method == "GET":
         form = n50sict3form()
         context = {
            'form': form
         }
         return render(request, 'management/ICT3FORM/ict3statusneo.html', context=context)
    else:
        form = n50sict3form(request.POST)
        if form.is_valid():
            conectar()
            sttstest = form.save()
            form = n50sict3form
            
        context = {
            'form': form
         }
        return render(request, 'management/ICT3FORM/ict3statusneo', context=context)

@login_required
def ict3statusm75(request):
    if request.method == "GET":
         form = m75ict3form()
         context = {
            'form': form
         }
         return render(request, 'management/ICT3FORM/ict3statusm75.html', context=context)
    else:
        form = m75ict3form(request.POST)
        if form.is_valid():
            conectar()
            sttstest = form.save()
            form = m75ict3form
        context = {
            'form': form
         }
        return render(request, 'management/ICT3FORM/ict3statusm75.html', context=context)

@login_required
def ict3statusideapad3i(request):
    if request.method == "GET":
         form = ideapad3iict3form()
         context = {
            'form': form
         }
         return render(request, 'management/ICT3FORM/ict3statusideapad3i.html', context=context)
    else:
        form = ideapad3iict3form(request.POST)
        if form.is_valid():
            comando = 'UPDATE ictmanagement.management_coberturatotal3i SET tested = tested-1 WHERE Id = 1'
            conectar()
            sttstest = form.save()
            form = ideapad3iict3form
        context = {
            'form': form
         }
        return render(atualizar(comando), 'management/ICT3FORM/ict3statusideapad3i.html', context=context)

@login_required
def ict3statusideapad3a(request):
    if request.method == "GET":
         form = ideapad3aict3form()
         context = {
            'form': form
         }
         return render(request, 'management/ICT3FORM/ict3statusideapad3a.html', context=context)
    else:
        form = ideapad3aict3form(request.POST)
        if form.is_valid():
            comando = 'UPDATE ictmanagement.management_coberturatotal3a SET tested = tested-1 WHERE Id = 1'
            conectar()
            sttstest = form.save()
            form = ideapad3aict3form
        context = {
            'form': form
         }
        return render(atualizar(comando), 'management/ICT3FORM/ict3statusideapad3a.html', context=context)


@login_required
def ict3statuse14(request):
    if request.method == "GET":
         form = e14ict3form()
         context = {
            'form': form
         }
         return render(request, 'management/ICT3FORM/ict3statuse14.html', context=context)
    else:
        form = e14ict3form(request.POST)
        if form.is_valid():
            comando = 'UPDATE ictmanagement.management_coberturatotale14 SET tested = tested-1 WHERE Id = 1'
            conectar()
            sttstest = form.save()
            form = e14ict3form
        context = {
            'form': form
         }
        return render(atualizar(comando), 'management/ICT3FORM/ict3statuse14.html', context=context)

@login_required
def ict3statusideapad1(request):
    if request.method == "GET":
         form = ideapad31ict3form()
         context = {
            'form': form
         }
         return render(request, 'management/ICT3FORM/ict3statusideapad1.html', context=context)
    else:
        form = ideapad31ict3form(request.POST)
        if form.is_valid():
            comando = 'UPDATE ictmanagement.management_coberturatotalideapad1 SET tested = tested-1 WHERE Id = 1'
            conectar()
            sttstest = form.save()
            form = ideapad31ict3form
        context = {
            'form': form
         }
        return render(atualizar(comando), 'management/ICT3FORM/ict3statusideapad1.html', context=context)


###formularios fim




### CHARTS inicio

@login_required
def n50schart(request):
    placeds = list(coberturatotalN50s.objects.values('placeds').values_list('placeds', flat=True))
    testable = list(coberturatotalN50s.objects.values('testable').values_list('testable', flat=True))
    tested = list(coberturatotalN50s.objects.values('tested').values_list('tested', flat=True))
    labels = ['Montados','Testaveis','Testados']
    data = []
    data.append(placeds)
    data.append(testable)
    data.append(tested)
    print(data)
    print(labels)
    data_json = {'data':data, 'labels':labels}
    return JsonResponse(data_json)

@login_required
def m75chart(request):
    placeds = list(coberturatotalm75.objects.values('placeds').values_list('placeds', flat=True))
    testable = list(coberturatotalm75.objects.values('testable').values_list('testable', flat=True))
    tested = list(coberturatotalm75.objects.values('tested').values_list('tested', flat=True))
    labels = ['Montados','Testaveis','Testados']
    data = [placeds,testable,tested]
    print(data)
    print(labels)
    data_json = {'data':data, 'labels':labels}
    return JsonResponse(data_json)

@login_required
def ideapad3ichart(request):
    placeds = list(coberturatotal3i.objects.values('placeds').values_list('placeds', flat=True))
    testable = list(coberturatotal3i.objects.values('testable').values_list('testable', flat=True))
    tested = list(coberturatotal3i.objects.values('tested').values_list('tested', flat=True))
    labels = ['Montados','Testaveis','Testados']
    data = [placeds,testable,tested]
    print(data)
    print(labels)
    data_json = {'data':data, 'labels':labels}
    return JsonResponse(data_json)

@login_required
def ideapad3achart(request):
    placeds = list(coberturatotal3a.objects.values('placeds').values_list('placeds', flat=True))
    testable = list(coberturatotal3a.objects.values('testable').values_list('testable', flat=True))
    tested = list(coberturatotal3a.objects.values('tested').values_list('tested', flat=True))
    labels = ['Montados','Testaveis','Testados']
    data = [placeds,testable,tested]
    print(data)
    print(labels)
    data_json = {'data':data, 'labels':labels}
    return JsonResponse(data_json)

@login_required
def ideapad1chart(request):
    placeds = list(coberturatotalideapad1.objects.values('placeds').values_list('placeds', flat=True))
    testable = list(coberturatotalideapad1.objects.values('testable').values_list('testable', flat=True))
    tested = list(coberturatotalideapad1.objects.values('tested').values_list('tested', flat=True))
    labels = ['Montados','Testaveis','Testados']
    data = [placeds,testable,tested]
    print(data)
    print(labels)
    data_json = {'data':data, 'labels':labels}
    return JsonResponse(data_json)

@login_required
def e14chart(request):
    placeds = list(coberturatotale14.objects.values('placeds').values_list('placeds', flat=True))
    testable = list(coberturatotale14.objects.values('testable').values_list('testable', flat=True))
    tested = list(coberturatotale14.objects.values('tested').values_list('tested', flat=True))
    labels = ['Montados','Testaveis','Testados']
    data = [placeds,testable,tested]
    print(data)
    print(labels)
    data_json = {'data':data, 'labels':labels}
    return JsonResponse(data_json)

### CHARTS fim

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class usuariocreate(CreateView):
    template_name = "management/usuariocreate.html"
    form_class = usuarioform
    success_url = reverse_lazy('login')

class passwordchangeview(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('login')



#DELETE DE REGISTROS ICT1

class n50sict1del(DeleteView):
    model = n50sict1
    template_name = 'management/ict1delete/n50sict1del.html'
    success_url = reverse_lazy('n50sict1list')
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(n50sict1del,self).form_valid(form)


class m75ict1del(DeleteView):
    model = m75ict1
    template_name = 'management/ict1delete/m75ict1del.html'
    success_url = reverse_lazy('m75ict1list')
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(m75ict1del,self).form_valid(form)



class ideapad3aict1del(DeleteView):
    model =ideapad3aict1
    template_name = 'management/ict1delete/ideapad3aict1del.html'
    success_url = reverse_lazy('ideapad3aict1list')
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(ideapad3aict1del,self).form_valid(form)



class ideapad3iict1del(DeleteView):
    model = ideapad3iict1
    template_name = 'management/ict1delete/ideapad3iict1del.html'
    success_url = reverse_lazy('ideapad3iict1list')
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(ideapad3iict1del,self).form_valid(form)



class ideapad1ict1del(DeleteView):
    model = ideapad31ict1
    template_name = 'management/ict1delete/ideapad1ict1del.html'
    success_url = reverse_lazy('ideapad1ict1list')
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(ideapad1ict1del,self).form_valid(form)


class e14ict1del(DeleteView):
    model = e14ict1
    template_name = 'management/ict1delete/e14ict1del.html'
    success_url = reverse_lazy('e14ict1list')
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(e14ict1del,self).form_valid(form)



#DELETE DE REGISTROS ICT2


################chart
class n50sict2del(DeleteView):
    model = n50sict2
    template_name = 'management/ict2delete/n50sict2del.html'
    success_url = reverse_lazy('n50sict2list')
    def form_valid(self, form):
        comando = 'UPDATE ictmanagement.management_coberturatotaln50s SET tested = tested+1 WHERE Id = 1'
        conectar()
        atualizar(comando)
        messages.success(self.request, "The task was deleted successfully.")
        return super(n50sict2del,self).form_valid(form)

################chart
class m75ict2del(DeleteView):
    model = m75ict2
    template_name = 'management/ict2delete/m75ict2del.html'
    success_url = reverse_lazy('m75ict2list')
    def form_valid(self, form):
        comando = 'UPDATE ictmanagement.management_coberturatotalm75 SET tested = tested+1 WHERE Id = 1'
        conectar()
        atualizar(comando)
        messages.success(self.request, "The task was deleted successfully.")
        return super(m75ict2del,self).form_valid(form)



class ideapad3aict2del(DeleteView):
    model =ideapad3aict2
    template_name = 'management/ict2delete/ideapad3aict2del.html'
    success_url = reverse_lazy('ideapad3aict2list')
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(ideapad3aict2del,self).form_valid(form)



class ideapad3iict2del(DeleteView):
    model = ideapad3iict2
    template_name = 'management/ict2delete/ideapad3iict2del.html'
    success_url = reverse_lazy('ideapad3iict2list')
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(ideapad3iict2del,self).form_valid(form)



class ideapad1ict2del(DeleteView):
    model = ideapad31ict2
    template_name = 'management/ict2delete/ideapad2ict2del.html'
    success_url = reverse_lazy('ideapad1ict2list')
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(ideapad1ict2del,self).form_valid(form)


class e14ict2del(DeleteView):
    model = e14ict2
    template_name = 'management/ict2delete/e14ict2del.html'
    success_url = reverse_lazy('e14ict2list')
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(e14ict2del,self).form_valid(form)



#DELETE DE REGISTROS ICT3

class n50sict3del(DeleteView):
    model = n50sict3
    template_name = 'management/ict3delete/n50sict3del.html'
    success_url = reverse_lazy('m75ict3list')
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(n50sict3del,self).form_valid(form)


class m75ict3del(DeleteView):
    model = m75ict3
    template_name = 'management/ict3delete/m75ict3del.html'
    success_url = reverse_lazy('n50schart')
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(m75ict3del,self).form_valid(form)


################chart
class ideapad3aict3del(DeleteView):
    model =ideapad3aict3
    template_name = 'management/ict3delete/ideapad3aict3del.html'
    success_url = reverse_lazy('ideapad3aict3list')
    def form_valid(self, form):
        comando = 'UPDATE ictmanagement.management_coberturatotal3a SET tested = tested+1 WHERE Id = 1'
        conectar()
        atualizar(comando)
        messages.success(self.request, "The task was deleted successfully.")
        return super(ideapad3aict3del,self).form_valid(form)


################chart
class ideapad3iict3del(DeleteView):
    model = ideapad3iict3
    template_name = 'management/ict3delete/ideapad3iict3del.html'
    success_url = reverse_lazy('ideapad3iict3list')
    def form_valid(self, form):
        comando = 'UPDATE ictmanagement.management_coberturatotal3i SET tested = tested+1 WHERE Id = 1'
        conectar()
        atualizar(comando)
        messages.success(self.request, "The task was deleted successfully.")
        return super(ideapad3iict3del,self).form_valid(form)


################chart
class ideapad1ict3del(DeleteView):
    model = ideapad31ict3
    template_name = 'management/ict3delete/ideapad1ict3del.html'
    success_url = reverse_lazy('ideapad1ict3list')
    def form_valid(self, form):
        comando = 'UPDATE ictmanagement.management_coberturatotalideapad1 SET tested = tested+1 WHERE Id = 1'
        conectar()
        atualizar(comando)
        messages.success(self.request, "The task was deleted successfully.")
        return super(ideapad1ict3del,self).form_valid(form)

################chart
class e14ict3del(DeleteView):
    model = e14ict3
    template_name = 'management/ict3delete/e14ict3del.html'
    success_url = reverse_lazy('e14ict3list')
    def form_valid(self, form):
        comando = 'UPDATE ictmanagement.management_coberturatotale14 SET tested = tested+1 WHERE Id = 1'
        conectar()
        atualizar(comando)
        messages.success(self.request, "The task was deleted successfully.")
        return super(e14ict3del,self).form_valid(form)


### list views

#ict1

class n50sict1list(ListView):
    model = n50sict1
    template_name = 'management/ict1list/n50sict1list.html'


class m75ict1list(ListView):
    model = m75ict1
    template_name = 'management/ict1list/m75ict1list.html'


class ideapad3iict1list(ListView):
    model = ideapad3iict1
    template_name = 'management/ict1list/ideapad3iict1list.html'


class ideapad3aict1list(ListView):
    model = ideapad3aict1
    template_name = 'management/ict1list/ideapad3aict1list.html'


class ideapad1ict1list(ListView):
    model = ideapad31ict1
    template_name = 'management/ict1list/ideapad1ict1list.html'

class e14ict1list(ListView):
    model = e14ict1
    template_name = 'management/ict1list/e14ict1list.html'


#ict2

class n50sict2list(ListView):
    model = n50sict2
    template_name = 'management/ict2list/n50sict2list.html'


class m75ict2list(ListView):
    model = m75ict2
    template_name = 'management/ict2list/m75ict2list.html'


class ideapad3iict2list(ListView):
    model = ideapad3iict2
    template_name = 'management/ict2list/ideapad3iict2list.html'


class ideapad3aict2list(ListView):
    model = ideapad3aict2
    template_name = 'management/ict2list/ideapad3aict2list.html'


class ideapad1ict2list(ListView):
    model = ideapad31ict2
    template_name = 'management/ict2list/ideapad1ict2list.html'

class e14ict2list(ListView):
    model = e14ict2
    template_name = 'management/ict2list/e14ict2list.html'


#ict3

class n50sict3list(ListView):
    model = n50sict3
    template_name = 'management/ict3list/n50sict3list.html'


class m75ict3list(ListView):
    model = m75ict3
    template_name = 'management/ict3list/m75ict3list.html'


class ideapad3iict3list(ListView):
    model = ideapad3iict3
    template_name = 'management/ict3list/ideapad3iict3list.html'


class ideapad3aict3list(ListView):
    model = ideapad3aict3
    template_name = 'management/ict3list/ideapad3aict3list.html'


class ideapad1ict3list(ListView):
    model = ideapad31ict3
    template_name = 'management/ict3list/ideapad1ict3list.html'

class e14ict3list(ListView):
    model = e14ict3
    template_name = 'management/ict3list/e14ict3list.html'


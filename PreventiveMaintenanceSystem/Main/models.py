from django.db import models
import datetime
from datetime import timedelta
from datetime import datetime, date, timedelta
from PIL import Image
from datetime import date, timedelta, timezone
import datetime

class DateIntegerField(models.IntegerField):
    def validate(self, value, model_instance):
        if not isinstance(value, int) or not isinstance(datetime.date.fromtimestamp(value), datetime.date):
            raise ValueError("Este campo deve ser um timestamp de data válida")
        super().validate(value, model_instance)

class maquina(models.Model):
    nome = models.CharField(max_length=255)
    prazo = models.DateField(null=True)
    periodicidade = models.IntegerField(null=True)
    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.prazo = date.today() + timedelta(days=self.periodicidade)
        super(maquina, self).save(*args, **kwargs)

    def remaining_days(self):
            deadline_datetime = datetime.datetime.combine(self.prazo, datetime.time.min)
            remaining_time = deadline_datetime - datetime.datetime.now()
            remaining_days = remaining_time.days
            remaining_seconds = remaining_time.seconds
            remaining_hours, remaining_minutes = divmod(remaining_seconds, 3600)
            remaining_days += remaining_hours // 24
            remaining_hours = remaining_hours % 24
            return (remaining_days)
    def remaining_hours(self):
        deadline_datetime = datetime.datetime.combine(self.prazo, datetime.time.min)
        remaining_time = deadline_datetime - datetime.datetime.now()
        remaining_days = remaining_time.days
        remaining_seconds = remaining_time.seconds
        remaining_hours, remaining_minutes = divmod(remaining_seconds, 3600)
        remaining_days += remaining_hours // 24
        remaining_hours = remaining_hours % 24
        return (remaining_hours)
        
class Perfil(models.Model):
    item = models.OneToOneField(maquina, on_delete=models.CASCADE, name='Referencia')
    Nome = models.CharField(max_length=255)
    caracteristicasGerais = models.TextField(max_length=1000,blank=True, null=True, name='Informações')
    Foto = models.ImageField(upload_to='perfil/', blank=True, null=True)


    def __str__(self):
        return self.Nome

    def save(self, *args, **kwargs):
        self.id = self.Referencia_id
        super().save(*args, **kwargs)
        
class tarefa(models.Model):
    STATUS_CHOICES = [
    ('Pendente', 'Pendente'),
    ('Agendado', 'Agendado'),
    ('Concluida', 'Concluida'),]

    item = models.ForeignKey(maquina, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, null=True, default='Agendado')
    
    def status_css_class(self):
        if self.status == 'Concluida':
            return 'success'
        elif self.status == 'Pendente':
            return 'pendente'
        else:
            print('ok')
    def __str__(self):
        return self.nome
    def remaining_days(self):
            deadline_datetime = datetime.datetime.combine(self.item.prazo, datetime.time.min)
            remaining_time = deadline_datetime - datetime.datetime.now()
            remaining_days = remaining_time.days
            return (remaining_days)
    def remaining_hours(self):
        deadline_datetime = datetime.datetime.combine(self.item.prazo, datetime.time.min)
        remaining_hours = remaining_hours % 24
        return (remaining_hours)


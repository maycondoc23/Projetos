from django.db import models
from datetime import date, time, datetime
from django.contrib.auth.models import User



### dict

FAIL_CHOICES = (
    ('preshort' , 'preshort'),
    ('short' , 'short'),
    ('analog' , 'analog'),
    ('vectorless' , 'vectorless'),
)

SKIP_CHOICES = (
    ('ON' , 'ON'),
    ('OFF' , 'OFF')
)

MODELOS_CHOICES = (
    ('NEO50s', 'NEO50s'),
    ('M75', 'M75'),
    ('IDEAPAD3i', 'IDEAPAD3i'),
    ('IDEAPAD3a', 'IDEAPAD3a'),
    ('IDEAPAD1', 'IDEAPAD1'),
    ('E14', 'E14'),
)

STATUS_CHOICES = (
    ('ON', 'ON'),
    ('OFF', 'OFF')
)

#ict1


class n50sict1(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente

class ideapad3iict1(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente

class ideapad3aict1(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente

class ideapad31ict1(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente

class e14ict1(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente

class m75ict1(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente

#ict2

class n50sict2(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente

class ideapad3iict2(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente

class ideapad3aict2(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente

class ideapad31ict2(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente

class e14ict2(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente

class m75ict2(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente

#ict3



class n50sict3(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente

class ideapad3iict3(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente

class ideapad3aict3(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente

class ideapad31ict3(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente

class e14ict3(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente

class m75ict3(models.Model):
    componente = models.CharField(max_length=30)
    fail_in=models.CharField(max_length=30,name= "Falha", choices=FAIL_CHOICES)
    reason=models.CharField(max_length=50, name="Motivo")
    data=models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.componente




#cover

class coberturatotalN50s(models.Model):
    placeds=models.IntegerField()
    testable=models.IntegerField()
    tested=models.IntegerField()
    boardname=models.CharField(max_length=30)
    
    def __str__(self):
        return self.boardname    

class coberturatotalm75(models.Model):
    placeds=models.IntegerField()
    testable=models.IntegerField()
    tested=models.IntegerField()
    boardname=models.CharField(max_length=30)
    
    def __str__(self):
        return self.boardname    

class coberturatotal3i(models.Model):
    placeds=models.IntegerField()
    testable=models.IntegerField()
    tested=models.IntegerField()
    boardname=models.CharField(max_length=30)
    
    def __str__(self):
        return self.boardname    

class coberturatotal3a(models.Model):
    placeds=models.IntegerField()
    testable=models.IntegerField()
    tested=models.IntegerField()
    boardname=models.CharField(max_length=30)
    
    def __str__(self):
        return self.boardname    

class coberturatotalideapad1(models.Model):
    placeds=models.IntegerField()
    testable=models.IntegerField()
    tested=models.IntegerField()
    boardname=models.CharField(max_length=30)
    
    def __str__(self):
        return self.boardname    

class coberturatotale14(models.Model):
    placeds=models.IntegerField()
    testable=models.IntegerField()
    tested=models.IntegerField()
    boardname=models.CharField(max_length=30)
    
    def __str__(self):
        return self.boardname    




#others

class datetime(models.Model):
    models.DateTimeField(auto_now_add=True)

class users(models.Model):
    username = models.CharField(max_length=30, null=True)
    email = models.OneToOneField(User, on_delete=models.CASCADE)
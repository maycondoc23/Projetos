from django import forms
from .models import ideapad31ict3, ideapad3aict3, ideapad3iict3, m75ict3, e14ict3, n50sict3,m75ict1, e14ict1, ideapad31ict1, ideapad31ict2, ideapad3aict1, ideapad3aict2, ideapad3iict1, ideapad3iict2, n50sict1 ,n50sict2, m75ict2, coberturatotalN50s, coberturatotal3i, coberturatotalm75, coberturatotale14, coberturatotal3a, coberturatotalideapad1, ideapad31ict2, ideapad3aict2, ideapad3iict2, e14ict2
import datetime
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, UserModel, UsernameField
from django.contrib.auth.models import User

#ict1
class n50sict1form(forms.ModelForm):
    class Meta:
        model = n50sict1
        fields = "__all__"
     
class m75ict1form(forms.ModelForm):
    class Meta:
        model = m75ict1
        fields = "__all__"
         
class ideapad3iict1form(forms.ModelForm):
    class Meta:
        model = ideapad3iict1
        fields = "__all__"
             
class ideapad3aict1form(forms.ModelForm):
    class Meta:
        model = ideapad3aict1
        fields = "__all__"
               
class ideapad31ict1form(forms.ModelForm):
    class Meta:
        model = ideapad31ict1
        fields = "__all__"
                   
class e14ict1form(forms.ModelForm):
    class Meta:
        model = e14ict1
        fields = "__all__"




#ict2
class n50sict2form(forms.ModelForm):
    class Meta:
        model = n50sict2
        fields = "__all__"
     
class m75ict2form(forms.ModelForm):
    class Meta:
        model = m75ict2
        fields = "__all__"
         
class ideapad3iict2form(forms.ModelForm):
    class Meta:
        model = ideapad3iict2
        fields = "__all__"
             
class ideapad3aict2form(forms.ModelForm):
    class Meta:
        model = ideapad3aict2
        fields = "__all__"
               
class ideapad31ict2form(forms.ModelForm):
    class Meta:
        model = ideapad31ict2
        fields = "__all__"
                   
class e14ict2form(forms.ModelForm):
    class Meta:
        model = e14ict2
        fields = "__all__"


#ict3
class n50sict3form(forms.ModelForm):
    class Meta:
        model = n50sict3
        fields = "__all__"
     
class m75ict3form(forms.ModelForm):
    class Meta:
        model = m75ict3
        fields = "__all__"
         
class ideapad3iict3form(forms.ModelForm):
    class Meta:
        model = ideapad3iict3
        fields = "__all__"
             
class ideapad3aict3form(forms.ModelForm):
    class Meta:
        model = ideapad3aict3
        fields = "__all__"
               
class ideapad31ict3form(forms.ModelForm):
    class Meta:
        model = ideapad31ict3
        fields = "__all__"
                   
class e14ict3form(forms.ModelForm):
    class Meta:
        model = e14ict3
        fields = "__all__"





#cover
class coberturatotaln50sform(forms.ModelForm):
    class Meta:
        model = coberturatotalN50s
        fields = "__all__"
    
class coberturatotalm75form(forms.ModelForm):
    class Meta:
        model = coberturatotalm75
        fields = "__all__"
      
class coberturatotal3iform(forms.ModelForm):
    class Meta:
        model = coberturatotal3i
        fields = "__all__"
          
class coberturatotal3aform(forms.ModelForm):
    class Meta:
        model = coberturatotal3a
        fields = "__all__"
          
class coberturatotale14form(forms.ModelForm):
    class Meta:
        model = coberturatotale14
        fields = "__all__"
         
class coberturatotalideapad1form(forms.ModelForm):
    class Meta:
        model = coberturatotalideapad1
        fields = "__all__"
    
    


class usuarioform(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50) 
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class edituserprofile(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter your username"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your first name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your last name"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your username"}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

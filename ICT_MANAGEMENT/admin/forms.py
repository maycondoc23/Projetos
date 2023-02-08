from django import forms
from .models import coberturatotaN50s
import datetime

 
# class Regform(forms.ModelForm):
#     class Meta:
#         model = Regfail
#         fields = 'tittle', 'description'

# class skipform(forms.ModelForm):
#     class Meta:
#         model = skiptestn50s
#         fields = "__all__"

    
class coberturatotalform(forms.ModelForm):
    class Meta:
        model = coberturatotaN50s
        fields = "__all__"
    

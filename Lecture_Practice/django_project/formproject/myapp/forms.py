from django import forms
from .models import *

class studinfoForm(forms.ModelForm):
    class Meta:
        model= studinfo
        fields='__all__'
    
class updateForm(forms.ModelForm):
    class Meta:
        model=studinfo
        fields='__all__'

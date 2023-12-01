from django import forms
from .models import *

class signupform(forms.ModelForm):
    class Meta:
        model=signupdata
        fields='__all__'
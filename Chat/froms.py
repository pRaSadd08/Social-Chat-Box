from django import forms
from .models import Social

class Form(forms.ModelForm):
    class Meta:
        model=Social
        fields= '__all__'
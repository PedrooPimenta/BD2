from django import forms
from .models import Monografias
class MonografiaForm(forms.ModelForm):
    class Meta:
        model = Monografias
        fields = '__all__'

  
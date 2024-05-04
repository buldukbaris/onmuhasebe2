# forms.py
from django import forms
from .models import Cari

class CariForm(forms.ModelForm):
    class Meta:
        model = Cari
        fields = '__all__'  # Tüm alanları içermesi için '__all__' kullanabilirsiniz

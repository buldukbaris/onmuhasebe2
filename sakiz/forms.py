from django import forms
from .models import SakizMakinesi

# forms.py


class SakizMakinesiForm(forms.ModelForm):
    class Meta:
        model = SakizMakinesi
        fields = '__all__'  # Tüm alanları kullanmak istiyorsanız


        
 

# satislar/forms.py

from django import forms
from .models import Satis

class SatisEkleForm(forms.ModelForm):
    class Meta:
        model = Satis
        fields = '__all__'

    kdv_tipi = forms.ChoiceField(
        choices=[('kdv_dahil', 'KDV Dahil'), ('kdv_haric', 'KDV Hariç')],
        widget=forms.RadioSelect,
        initial='kdv_haric',
        label='KDV Tipi'
    )


from django import forms
from .models import SatinAlma

class SatinAlmaForm(forms.ModelForm):
    class Meta:
        model = SatinAlma
        fields = '__all__'

    kdv_tipi = forms.ChoiceField(
        choices=[('kdv_dahil', 'KDV Dahil'), ('kdv_haric', 'KDV Hariç')],
        widget=forms.RadioSelect,
        initial='kdv_haric',
        label='KDV Tipi'
    )

from django import forms
from satinalma.models import SatinAlma
from satislar.models import Satis
from cariler.models import Cari
from sakiz.models import SakizMakinesi



class CariForm(forms.ModelForm):
    class Meta:
        model = Cari
        fields = ['cari_adi', 'vergi_dairesi', 'vergi_no', 'telefon', 'email', 'adres']


class MyFormWidget(forms.widgets.Input):
    template_name = 'widgets/my_form_widget.html'

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Kullanıcı Adı" 
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Parola"
    )

# onmuhasebe/forms.py



class MyFormWidget(forms.widgets.Input):
    template_name = 'widgets/my_form_widget.html'
    
    def __init__(self, attrs=None):
        default_attrs = {'class': 'form-control'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

class SatinAlmaForm(forms.ModelForm):
    stok_adi = forms.CharField(
        widget=MyFormWidget(attrs={'class': 'form-control', 'placeholder': 'Stok Adı', 'label': 'Stok Adı'})
    )
    miktar = forms.DecimalField(
        widget=MyFormWidget(attrs={'class': 'form-control', 'placeholder': 'Miktar', 'label': 'Miktar'})
    )
    birimi = forms.CharField(
        widget=MyFormWidget(attrs={'class': 'form-control', 'placeholder': 'Birimi', 'label': 'Birimi'})
    )
    kdv_orani = forms.DecimalField(
        widget=MyFormWidget(attrs={'class': 'form-control', 'placeholder': 'KDV Oranı', 'label': 'KDV Oranı'})
    )
    kdvhalis_fiyati = forms.DecimalField(
        widget=MyFormWidget(attrs={'class': 'form-control', 'placeholder': 'KDV Halis Fiyatı', 'label': 'KDV Halis Fiyatı'})
    )
    kdvdalis_fiyati = forms.DecimalField(
        widget=MyFormWidget(attrs={'class': 'form-control', 'placeholder': 'KDV Dahil Fiyatı', 'label': 'KDV Dahil Fiyatı'})
    )
    cari_adi = forms.CharField(
        widget=MyFormWidget(attrs={'class': 'form-control', 'placeholder': 'Cari Adı', 'label': 'Cari Adı'})
    )

    is_borc = forms.BooleanField(label='Borç', required=False)

    class Meta:
        model = SatinAlma
        fields = ['stok_adi', 'miktar', 'birimi', 'kdv_orani', 'kdvhalis_fiyati', 'kdvdalis_fiyati', 'cari_adi']

    def clean(self):
        cleaned_data = super().clean()
        is_borc = cleaned_data.get('is_borc')

        return cleaned_data    




class SatisEkleForm(forms.ModelForm):
    stok_adi = forms.CharField(
        widget=MyFormWidget(attrs={'class': 'form-control', 'placeholder': 'Stok Adı', 'label': 'Stok Adı'})
    )
    miktar = forms.DecimalField(
        widget=MyFormWidget(attrs={'class': 'form-control', 'placeholder': 'Miktar', 'label': 'Miktar'})
    )
    birimi = forms.CharField(
        widget=MyFormWidget(attrs={'class': 'form-control', 'placeholder': 'Birimi', 'label': 'Birimi'})
    )
    kdv_orani = forms.DecimalField(
        widget=MyFormWidget(attrs={'class': 'form-control', 'placeholder': 'KDV Oranı', 'label': 'KDV Oranı'})
    )
    kdvhalis_fiyati = forms.DecimalField(
        widget=MyFormWidget(attrs={'class': 'form-control', 'placeholder': 'KDV Halis Fiyatı', 'label': 'KDV Halis Fiyatı'})
    )
    kdvdalis_fiyati = forms.DecimalField(
        widget=MyFormWidget(attrs={'class': 'form-control', 'placeholder': 'KDV Dahil Fiyatı', 'label': 'KDV Dahil Fiyatı'})
    )
    cari_adi = forms.CharField(
        widget=MyFormWidget(attrs={'class': 'form-control', 'placeholder': 'Cari Adı', 'label': 'Cari Adı'})
    )

    class Meta:
        model = Satis
        fields = ['stok_adi', 'miktar', 'birimi', 'kdv_orani', 'kdvhalis_fiyati', 'kdvdalis_fiyati', 'cari_adi']



"""class SakizMakinesiForm(forms.ModelForm):
    marka = forms.CharField(
        widget=MyFormWidget(attrs={'class': 'form-control', 'placeholder': 'Marka', 'label': 'Marka'})
    )
    model = forms.CharField(
        widget=MyFormWidget(attrs={'class': 'form-control', 'placeholder': 'Model', 'label': 'Model'})
    )
    class Meta:
        model = SakizMakinesi
        fields = ['marka', 'model']"""





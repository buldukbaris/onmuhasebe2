# satisekle/views.py

from django.shortcuts import render,redirect
from .forms import SatisEkleForm

def satis_ekle_create(request):
    # Satış ekleme işlemleri burada yapılacak
    if request.method == 'POST':
        form = SatisEkleForm(request.POST)
        if form.is_valid():
            satis_ekle = form.save(commit=False)

            # KDV tipini kontrol et ve uygun şekilde kaydet
            kdv_tipi = form.cleaned_data.get('kdv_tipi')
            if kdv_tipi == 'kdv_dahil':
                satis_ekle.kdvdalis_fiyati = satis_ekle.kdv_haric_alis_fiyati_hesapla()
            satis_ekle.save()

            return redirect('satis_ekle_list')  # Başka bir sayfaya yönlendirilebilir

    else:
        form = SatisEkleForm()

    return render(request, 'satis_ekle_create.html', {'form': form})



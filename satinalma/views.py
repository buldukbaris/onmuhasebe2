from django.shortcuts import render, redirect
from .forms import SatinAlmaForm

def satin_alma_create(request):
    if request.method == 'POST':
        form = SatinAlmaForm(request.POST)
        if form.is_valid():
            satin_alma = form.save(commit=False)

            # KDV tipini kontrol et ve uygun şekilde kaydet
            kdv_tipi = form.cleaned_data.get('kdv_tipi')
            if kdv_tipi == 'kdv_dahil':
                satin_alma.kdvdalis_fiyati = satin_alma.kdv_haric_alis_fiyati_hesapla()
            satin_alma.save()

            return redirect('satin_alma_list')  # Başka bir sayfaya yönlendirilebilir

    else:
        form = SatinAlmaForm()

    return render(request, 'satin_alma_create.html', {'form': form})

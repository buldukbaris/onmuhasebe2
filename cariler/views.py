from django.shortcuts import render

# Create your views here.
def cari_ekle(request):
    cari_form = CariForm(request.POST or None)

    if request.method == 'POST' and cari_form.is_valid():
        cari_form.save()
        messages.success(request, "Cari Başarıyla Kaydedildi.")
        return redirect('cari_ekle')  # veya başka bir sayfaya yönlendir

    context = {
        'cari_form': cari_form,
    }

    return render(request, 'cari_ekle.html', context)
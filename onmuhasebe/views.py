from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm
from satinalma.forms import SatinAlmaForm
from satislar.forms import SatisEkleForm
from sakiz.forms import SakizMakinesiForm
from cariler.forms import CariForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from satinalma.models import SatinAlma
from satislar.models import Satis
from sakiz.models import SakizMakinesi
from cariler.models import Cari
from django.http import JsonResponse
import requests
from .trendyol_api import get_orders
from datetime import date, timedelta, datetime
from django.conf import settings
import json
from django.http import HttpResponse
from django.db.models import Sum




# views.py








def index(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        # Kullanıcı doğrulama işlemi
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Kullanıcı doğrulama başarılıysa oturum aç
            login(request, user)
            messages.success(request, "Başarıyla Giriş Yapıldı")
            return redirect("dashboard")
        else:
            messages.info(request, "Kullanıcı Adı veya Parola Hatalı")

    return render(request, "index.html", context)



def dashboard(request):
    current_datetime = datetime.now().strftime("%Y-%m-%d")



    context = {
        'current_datetime': current_datetime,
    }

    return render(request, 'dashboard.html', context)

def add_todo(request):
    if request.method == 'POST':
        todo_text = request.POST.get('todoText')
        # Veritabanına ekleme işlemi burada yapılabilir
        return JsonResponse({'status': 'success', 'todoText': todo_text})
    return JsonResponse({'status': 'error'})




# Alış Ekleme İşlemlerinin Yapıldığı Formum

def alisekle(request):
    keyword = request.GET.get("keyword")
    
    if keyword:
        satinalma_list = SatinAlma.objects.filter(stok_adi__contains=keyword).order_by('-id')
    else:
        satinalma_list = SatinAlma.objects.all().order_by('-id')

    form = SatinAlmaForm()

    if request.method == 'POST':
        form = SatinAlmaForm(request.POST)
        if form.is_valid():
            satin_alma = form.save(commit=False)
            kdv_tipi = form.cleaned_data.get('kdv_tipi')
            if kdv_tipi == 'kdv_dahil':
                satin_alma.kdvdalis_fiyati = satin_alma.kdv_haric_alis_fiyati_hesapla()
            satin_alma.save()
            messages.success(request, "Satın Alma İşlemi Başarıyla Kaydedildi.")
            return redirect("dashboard")

    context = {
        'form': form,
        'satinalma_list': satinalma_list,
    }

    return render(request, 'alisekle.html', context)

def updateAlisEkle(request, id):
    alis = get_object_or_404(SatinAlma, id=id)
    form = SatinAlmaForm(request.POST or None, request.FILES or None, instance=alis)
    if form.is_valid():
        form.save()
        messages.success(request, "Satın Alma Başarıyla Güncellendi")
        return redirect("dashboard")

    return render(request, 'updateAlis.html', {"form": form})

def deleteAlisEkle(request, id):
    alis = get_object_or_404(SatinAlma, id=id)
    alis.delete()
    messages.success(request,"Satın Alma Kaydı Başarıyla Silindi")
    return redirect('dashboard')





# Satış Ekleme İşlemlerinin Yapıldığı Formum

def satisekle(request):
    keyword = request.GET.get("keyword")
    
    if keyword:
        satislar_list = Satis.objects.filter(stok_adi__contains=keyword).order_by('-id')
    else:
        satislar_list = Satis.objects.all().order_by('-id')

    form = SatisEkleForm(request.POST or None)

    if request.method == 'POST':
        form = SatisEkleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Satış İşlemi Başarıyla Kaydedildi.")
            return redirect("dashboard")

    toplam_satis_miktari = Satis.objects.aggregate(toplam=Sum('tutari_kdvharic'))['toplam']

    context = {
        'form': form,
        'satislar_list': satislar_list,
        'toplam_satis_miktari': toplam_satis_miktari,
    }

    return render(request, 'satisekle.html', context)

def satislar_tarihe_gore(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        satislar_list = Satis.objects.filter(created_date__range=[start_date, end_date])
        context = {
            'satislar_list': satislar_list,
        }
        return render(request, 'satislar_tarihe_gore.html', context)
    else:
        return render(request, 'satislar_tarihe_gore.html')

def updateSatislar(request, id):
    satis = get_object_or_404(Satis, id=id)
    form = SatisEkleForm(request.POST or None, request.FILES or None, instance=satis)
    if form.is_valid():
        form.save()
        messages.success(request, "Satış İşlemi Başarıyla Güncellendi")
        return redirect("dashboard")

    return render(request, 'updateSatis.html', {"form": form})

def deleteSatislar(request, id):
    satis = get_object_or_404(Satis, id=id)
    satis.delete()
    messages.success(request,"Satış Kaydı Başarıyla Silindi")
    return redirect('dashboard')



# views.py




# ...

def convert_timestamp_to_datetime(timestamp):
    try:
        # Timestamp'ı milisaniyeden saniyeye çevir
        timestamp_seconds = timestamp / 1000.0
        # Timestamp'ı kullanarak bir tarih nesnesi oluştur
        date_object = datetime.utcfromtimestamp(timestamp_seconds)
        return date_object
    except Exception as e:
        # Hata durumunda None döndür
        print(f"Hata: {e}")
        return None


def trendyol_orders(request):
    bugunun_tarihi = datetime.now()
    api_key = 'your_api_key'
    secret_key = 'your_secret_key'
    supplier_id = 'your_supplier_id'
    if bugunun_tarihi.month == 2 and bugunun_tarihi.day == 29:
        # Eğer bugün Şubat'ın 29'u ise, bir sonraki günü kullan
        bugunun_tarihi += timedelta(days=1)
    end_date = (bugunun_tarihi.replace(year=bugunun_tarihi.year + 1)).strftime('%Y-%m-%d')

    # Format hatasını önlemek için başlangıç tarihini datetime nesnesine dönüştür
    start_date = datetime.strptime('2024-03-01', '%Y-%m-%d').strftime('%Y-%m-%d')
    page_index = 1
    page_size = 10

    # Trendyol API'ye istek yap
    orders = get_orders(start_date, end_date, page_index, page_size)

    # Trendyol API'den gelen yanıtı konsola yazdır
    print('Trendyol API Yanıtı:', orders)

    # ...

    if orders and 'error' not in orders:
        # İsteğe bağlı olarak sipariş verilerini işleyebilirsin.
        # Örneğin, bir şablona göndererek frontend tarafında görüntüleme yapabilirsiniz.
        for order in orders:
            claim_date_timestamp = order.get("claimDate", 0)
            order_date_timestamp = order.get("orderDate", 0)

            claim_date = convert_timestamp_to_datetime(claim_date_timestamp)
            order_date = convert_timestamp_to_datetime(order_date_timestamp)

            print(f"Claim Date: {claim_date}, Order Date: {order_date}")

        # Sipariş değişkeninin içeriğini konsola yazdır
        print('Sipariş İçeriği:', orders)

        context = {
            'trendyol_data': orders,
        }
        return render(request, 'trendyol.html', context)
    else:
        print('Trendyol API Hatası:', orders)
        return JsonResponse({'error': 'Siparişler alınamadı'})
    



    


# Sakız Makinesi Kayıt İşlemlerinin Yapıldığı Formum


def sakiz(request):
    keyword = request.GET.get("keyword")
    
    if keyword:
        sakizmakinesi_list = SakizMakinesi.objects.filter(cari__cari_adi__contains=keyword)
    else:
        sakizmakinesi_list = SakizMakinesi.objects.all()

    form = SakizMakinesiForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Ciro kaydedildi.')
            return redirect("sakiz")

    # Gün bazında toplam cirolar
    ciro_gun = SakizMakinesi.objects.values('created_date').annotate(toplam_ciro=Sum('ciroBuldukTL')).order_by('-created_date')

    # Ay bazında toplam cirolar
    ciro_ay = SakizMakinesi.objects.values('created_date__month').annotate(toplam_ciro=Sum('ciroBuldukTL')).order_by('-created_date__month')

    # Yıl bazında toplam cirolar
    ciro_yil = SakizMakinesi.objects.values('created_date__year').annotate(toplam_ciro=Sum('ciroBuldukTL')).order_by('-created_date__year')

    context = {
        'form': form,
        'sakizmakinesi_list': sakizmakinesi_list,
        'ciro_gun': ciro_gun,
        'ciro_ay': ciro_ay,
        'ciro_yil': ciro_yil,
    }

    return render(request, 'sakiz.html', context)


def deleteSakiz(request, id):
    sakiz = get_object_or_404(SakizMakinesi, id=id)
    sakiz.delete()
    messages.success(request, "Sakız Makinesi Kaydı Başarıyla Silindi")
    return redirect("sakiz")


def updateSakiz(request, id):
    sakiz = get_object_or_404(SakizMakinesi, id=id)
    form = SakizMakinesiForm(request.POST or None, instance=sakiz)
    if form.is_valid():
        form.save()
        messages.success(request, "Sakız Makinesi Başarıyla Güncellendi")
        return redirect("sakiz")

    return render(request, 'updateSakiz.html', {"form": form})




# Cari Kayıt İşlemlerinin Yapıldığı Formum

def cari_form(request):
    keyword = request.GET.get("keyword")
    
    if keyword:
        cari_list = Cari.objects.filter(cari_adi__contains=keyword).order_by('-id')
    else:
        cari_list = Cari.objects.all().order_by('-id')

    form = CariForm()

    if request.method == 'POST':
        form = CariForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form kaydedildi.')
            return redirect('cari_form')

    return render(request, 'cari_ekle.html', {'form': form, 'cari_list': cari_list})

def updateCariEkle(request, id):
     cari = get_object_or_404(Cari, id=id)
     form = CariForm(request.POST or None, request.FILES or None, instance=cari)
     if form.is_valid():
         form.save()
         messages.success(request, "Cari Kayıt Başarıyla Güncellendi")
         return redirect("dashboard")
     return render(request, 'updateCari.html', {"form":form})

def deleteCariler(request, id):
    cari = get_object_or_404(Cari, id=id)
    cari.delete()
    messages.success(request,"Cari Başarıyla Silindi")
    return redirect('dashboard')









    


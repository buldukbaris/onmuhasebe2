"""
URL configuration for onmuhasebe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index, dashboard, alisekle, satisekle, trendyol_orders, sakiz, cari_form, updateSatislar, deleteSatislar, updateAlisEkle, deleteAlisEkle, updateCariEkle, deleteCariler, updateSakiz, deleteSakiz, add_todo




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('satinalma/alisekle/', alisekle, name='alisekle'),
    path('satislar/satisekle', satisekle, name='satisekle'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('trendyol_data/', trendyol_orders, name='trendyol_data'),
    path('sakiz/', sakiz, name='sakiz'),
    path('sakiz/sakiz/update/<int:id>/', updateSakiz, name='update_sakiz'),
    path('sakiz/sakiz/delete/<int:id>/', deleteSakiz, name='delete_sakiz'),
    path('cari_ekle/', cari_form, name='cari_form'),
    path('satislar/satinalma/update/<int:id>/', updateSatislar, name='update_satislar'),
    path('satislar/satinalma/delete/<int:id>/', deleteSatislar, name='delete_satislar'),
    path('satinalma/alisekle//update/<int:id>/', updateAlisEkle, name='update_alislar'),
    path('delete_alislar/<int:id>/', deleteAlisEkle, name='delete_alislar'),
    path('cariler/update/<int:id>/', updateCariEkle, name='update_cariler'),
    path('cariler/delete/<int:id>/', deleteCariler, name='delete_cariler'),
    path('add_todo/', add_todo, name='add_todo'),
    
    

]

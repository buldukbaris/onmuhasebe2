# sakiz/urls.py

from django.urls import path
from . import views

urlpatterns = [

    path('update/<int:id>/', views.updateSakiz, name='update_sakiz'),
    path('delete/<int:id>/', views.deleteSakiz, name='delete_sakiz'),
    # Sakiz uygulamasının URL'lerini burada tanımlayabilirsiniz
    # Örneğin, views.py içindeki bir view'e yönlendirebilirsiniz
]

from django.urls import path

from django.urls import include
from django.contrib import auth
import detection.views as views

app_name = 'detection'

urlpatterns = [
    path('', views.index, name='index'),
    path('result/<int:pk>/', views.result, name='result'),
    path('accounts/', include('django.contrib.auth.urls'))
]
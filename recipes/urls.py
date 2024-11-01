from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recepie/<slug:slug>', views.recepie_detail, name='recepie-detail-page')
]

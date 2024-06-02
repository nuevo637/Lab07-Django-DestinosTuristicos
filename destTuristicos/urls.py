from django.urls import path
from . import views

urlpatterns = [
    path('destinos', views.destinos , name='destinos')
]

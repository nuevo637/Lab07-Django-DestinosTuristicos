from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_destino , name='listar-destinos'),
    path('crear/', views.crear_destino , name='crear-destinos')
]

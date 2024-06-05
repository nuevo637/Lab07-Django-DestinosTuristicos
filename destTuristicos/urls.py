from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_destino, name='listar-destinos'),
    path('crear/', views.crear_destino, name='crear-destinos'),
    path('editar/', views.seleccionar_y_editar_destino, name='seleccionar-editar-destino'),
    path('editar/<int:pk>/', views.seleccionar_y_editar_destino, name='seleccionar-editar-destino-con-pk'),
    path('eliminar/', views.eliminar_destino, name='eliminar-destino'),
]
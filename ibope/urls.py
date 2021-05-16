from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/emissoras/')),
    path('emissoras/', views.lista_emissoras, name='emissoras'),
    path('audiencia/', views.lista_audiencia, name='audiencia'),
    path('cadastra_emissora/', views.cadastra_emissora, name='cad_emissora'),
    path('cadastra_audiencia/', views.cadastra_audiencia, name='cad_audiencia'),
    path('delete/<int:id_emissora>', views.delete_emissora),
    path('emissoras/edicao/', views.edicao_emissora),
    path('relatorio/', views.lista_relatorio),
]

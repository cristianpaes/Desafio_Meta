from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/emissoras/')),
    path('emissoras/', views.lista_emissoras),
    path('audiencia/', views.lista_audiencia)
]

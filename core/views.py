from django.shortcuts import render
from core.models import Emissora, Audiencia


def lista_emissoras(request):
    emissora = Emissora.objects.all()
    dados_emissora = {'emissora':emissora}
    return render(request,'emissoras.html', dados_emissora)

def lista_audiencia(request):
    audiencia = Audiencia.objects.all()
    dados_audiencia = {'audiencia':audiencia}
    return render(request, 'audiencia.html', dados_audiencia)

from django.shortcuts import render, redirect, get_object_or_404
from core.models import Emissora, Audiencia
from core.form import EmissoraForm, AudienciaForm


def lista_emissoras(request):
    emissora = Emissora.objects.all()
    dados_emissora = {'emissora':emissora}
    return render(request,'emissoras.html', dados_emissora)


def lista_audiencia(request):
    audiencia = Audiencia.objects.all()
    dados_audiencia = {'audiencia':audiencia}
    return render(request, 'audiencia.html', dados_audiencia)


def cadastra_emissora(request):
    form = EmissoraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('emissoras')
    return render(request, 'cadastra_emissora.html', {'form': form})


def cadastra_audiencia(request):
    form = AudienciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('audiencia')
    return render(request, 'cadastra_audiencia.html', {'form': form})


def delete_emissora(request, id_emissora):
    Emissora.objects.filter(id=id_emissora).delete()
    return redirect('/')


def lista_relatorio(request):
    pass


def edicao_emissora(request):
    #id_emissora = get_object_or_404(Emissora, pk=id)
    id_emissora = request.GET.get('id')
    form = EmissoraForm(request.POST or None, instance=id_emissora)
    if form.is_valid():
        form.save()
        return redirect('emissoras')
    return render(request, 'cadastra_emissora.html', {'form': form})

    """id_emissora = request.GET.get('id')
    dados = {}
    if id_emissora:
        dados['emissora'] = Emissora.objects.get(id=id_emissora)
    return render(request, 'cadastra_emissora.html', dados)"""



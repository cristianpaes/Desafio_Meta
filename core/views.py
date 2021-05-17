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
        '''
            Realizando a busca e filtrando na tabela
        '''
        busca = request.GET.get('search')
        if busca:
            nome_emissora = Emissora.objects.filter(nome__icontains=busca)
            audiencia = Audiencia.objects.filter(emissora_audiencia__in=nome_emissora)
        else:
            audiencia = Audiencia.objects.all()
        dados_audiencia = {'audiencia': audiencia}
        return render(request, 'relatorio.html', dados_audiencia)

def edicao_emissora(request):
    pass
    '''id_emissora = get_object_or_404(Emissora, pk=id)
    form = EmissoraForm(request.POST or None, instance=id_emissora)
    if form.is_valid():
        form.save()
        return redirect('emissoras')
    return render(request, 'cadastra_emissora.html', {'form': form})'''

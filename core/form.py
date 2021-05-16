from django import forms
from core.models import Emissora, Audiencia
from django.contrib.admin import widgets


class EmissoraForm(forms.ModelForm):
    class Meta:
        model = Emissora
        fields = ['nome']
        labels = {'nome': 'Emissora'}


    def clean_nome(self):
        nome_emissora = self.cleaned_data.get('nome')
        if '%' in nome_emissora or '#' in nome_emissora or '%' in nome_emissora or '(' in nome_emissora or ')' in nome_emissora or '@' in nome_emissora or '-' in nome_emissora or '|' in nome_emissora or '*' in nome_emissora or '+' in nome_emissora or '.' in nome_emissora:
             raise forms.ValidationError("Não utilize caracteres especiais.")
        else:
            return nome_emissora.upper()


class AudienciaForm(forms.ModelForm):
    class Meta:
        model = Audiencia
        fields = ['pontos_audiencia', 'data_hora_audiencia','emissora_audiencia']
        labels = {'pontos_audiencia': 'Pontos de Audiência', 'emissora_audiencia': 'Emissora', 'data_hora_audiencia': 'Data e Hora' }

    """def clean_data_hora_audiencia(self, nome_emissora=None):
        data_hora = self.cleaned_data['data_hora_audiencia']
        emissora_id = self.cleaned_data['emissora_audiencia']
        existe_data_hora = Audiencia.objects.filter(emissora_audiencia_id=emissora_id, data_hora_audiencia=data_hora).exists()
        if existe_data_hora == True:
            raise forms.ValidationError("Data e Hora já gravado para essa Emissora.")
        else:
            return nome_emissora"""
from django.db import models
from django.utils import timezone

class Emissora(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'emissora'

    def __str__(self):
        return self.nome


class Audiencia(models.Model):
    pontos_audiencia = models.IntegerField(blank=False, null=True)
    data_hora_audiencia = models.DateTimeField(default=timezone.now,verbose_name='Data e Hora da Audiência')
    emissora_audiencia = models.ForeignKey(Emissora, on_delete= models.CASCADE, verbose_name='Emissora')

    class Meta:
        db_table = 'audiencia'

    def __int__(self):
        return self.pontos_audiencia

    def get_data_hora_audiencia(self):
        return self.data_hora_audiencia.strftime('%d/%m/%Y - Hora: %H:%M')
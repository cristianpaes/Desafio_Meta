from django.contrib import admin
from core.models import Emissora, Audiencia

@admin.register(Emissora)
class EmissoraAdmin(admin.ModelAdmin):
    list_display = ['id','nome']

@admin.register(Audiencia)
class AudienciaAdmin(admin.ModelAdmin):
    list_display = ['id','pontos_audiencia','data_hora_audiencia', 'emissora_audiencia']
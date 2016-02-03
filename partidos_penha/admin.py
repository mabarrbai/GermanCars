from django.contrib import admin

from partidos_penha.models import Penha, Jugador

class PenhaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}

admin.site.register(Penha, PenhaAdmin)
admin.site.register(Jugador)
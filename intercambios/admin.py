from django.contrib import admin

from .models import Intercambio, Participante


class ParticipanteInline(admin.TabularInline):
    model = Participante
    extra = 1


class IntercambioAdmin(admin.ModelAdmin):
    inlines = [ParticipanteInline]


admin.site.register(Intercambio, IntercambioAdmin)

from django.contrib import admin

from .models import Intercambio, Participante


class ParticipanteInline(admin.StackedInline):
    model = Participante
    extra = 3


class IntercambioAdmin(admin.ModelAdmin):
    inlines = [ParticipanteInline]


admin.site.register(Intercambio, IntercambioAdmin)

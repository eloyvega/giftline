from rest_framework import serializers

from .models import Intercambio


class IntercambioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Intercambio
        fields = ([item for item in Intercambio._meta.get_all_field_names() if item not in ['lista']])

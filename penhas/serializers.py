from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Penha, Jugador


class PenhaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Penha
        fields = ('url', 'nombre', 'ciudad')


class JugadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jugador
        fields = ('url', 'nombre', 'apellidos', 'penha')
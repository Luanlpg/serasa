from rest_framework import serializers

from .models import Consulta

class ClimaTempoSerializer(serializers.Serializer):
    """
    Serializer de processo completo.
    """
    cidade = serializers.CharField(default=None)

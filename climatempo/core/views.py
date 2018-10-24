from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ClimaTempoSerializer

from .clima import ClimaTempo

from .models import Consulta


class ClimaTempoView(APIView):
    """
    View que lista agendamentos especificos, e permite alteraçẽs
    e edições no mesmo.
    """
    serializer_class = ClimaTempoSerializer

    def get_consulta(self):
        return Consulta.objects.all().last

    def get(self, request, format=None):
        consulta = self.get_consulta()
        serializer = self.serializer_class(consulta)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            c = ClimaTempo
            Consulta.objects.create(consulta=c.parser(self, request.data['cidade']))
            serializer.save()

        return Response(serializer.data)

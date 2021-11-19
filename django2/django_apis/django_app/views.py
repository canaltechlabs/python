from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Serie
from .serializers import SerieSerializer

# Create your views here.

@api_view(['GET'])
def listSeries(request):
    series = listarSeries()
    series_serializer = SerieSerializer(series, many=True)
    return JsonResponse(series_serializer.data, safe=False, status = 200)

@api_view(['GET'])
def serieDetail(request, id):
    series = listarSeries()
    for serie in series:
        if(serie.id == int(id)):
            serie_serializer = SerieSerializer(serie)
            return JsonResponse(serie_serializer.data, safe=False, status = 200)

    return JsonResponse({'message: ' : 'serie nao encontrada'}, safe=False, status = 404)

@api_view(['POST'])
def createSerie(request):
    print('Salvei a Serie')
    print(request.body)
    return JsonResponse( {'message: ' : 'Serie criada com sucesso'}, safe=False, status = 200)

def listarSeries():
    serie1 = Serie()
    serie1.id = 1
    serie1.titulo = 'Game of Thrones'
    serie1.sinopse = 'Disputa e muita morte'
    serie1.quantidade_episodios = 1500

    serie2 = Serie()
    serie2.id = 2
    serie2.titulo = 'La casa de Papel'
    serie2.sinopse = 'Ladrões legais'
    serie2.quantidade_episodios = 650

    lista = []
    lista.append(serie1)
    lista.append(serie1)

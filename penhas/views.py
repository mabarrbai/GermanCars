"""
	Fichero correspondiente a las funciones de las vistas del proyecto.
"""
from django.shortcuts import render
from .models import Jugador, Penha
from rest_framework import viewsets
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import PenhaSerializer

import random

def formar_equipos(request): 
	"""Forma aleatoriamente los equipos de una penha para el partido semanal."""
	#componentes = []
	componentes = ['Juan','Alfonso','Carlos','Pepe','Diego','Andres','Javier','Alex','Mariano','Hugo','Iván','Jesús','Piti','Fran','Alfredo','Ángel','Raúl','Salva']
      
	random.shuffle(componentes)	#mezcla los elementos de la lista,cambiando el orden
    
	jugadores = len(componentes)

	assert jugadores != 0
	print("Test superado con éxito")
	
	equipo1 = componentes[0:int(jugadores/2)]

	equipo2 = componentes[int(jugadores/2):]
	
	return render(request, 'formar_equipos.html',{'equipo1':equipo1,'equipo2':equipo2})
	

class JSONResponse(HttpResponse):
	"""
	Una respuesta HTTP que renderiza el contenido en JSON
	"""
	def __init__(self,data,**kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

	@csrf_exempt
	def lista_penha(request):
	    """
	    Lista el codigo de todas las penhas, o crea una nueva
	    """
	    if request.method == 'GET':
	        penhas = Penhas.objects.all()
	        serializer = PenhaSerializer(penhas, many=True)
	        return JSONResponse(serializer.data)

	    elif request.method == 'POST':
	        data = JSONParser().parse(request)
	        serializer = PenhaSerializer(data=data)
	        if serializer.is_valid():
	            serializer.save()
	            return JSONResponse(serializer.data, status=201)
	        return JSONResponse(serializer.errors, status=400)

	@csrf_exempt
	def penha_detail(request, pk):
	    """
	    Recupera,actualiza o borra el codigo de una penha
	    """
	    try:
	        penha = Penha.objects.get(pk=pk)
	    except Penha.DoesNotExist:
	        return HttpResponse(status=404)

	    if request.method == 'GET':
	        serializer = PenhaSerializer(penha)
	        return JSONResponse(serializer.data)

	    elif request.method == 'PUT':
	        data = JSONParser().parse(request)
	        serializer = PenhaSerializer(penha, data=data)
	        if serializer.is_valid():
	            serializer.save()
	            return JSONResponse(serializer.data)
	        return JSONResponse(serializer.errors, status=400)

	    elif request.method == 'DELETE':
	        penha.delete()
	        return HttpResponse(status=204)

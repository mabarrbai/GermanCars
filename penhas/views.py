"""
	Fichero correspondiente a las funciones de las vistas del proyecto.
"""
from django.shortcuts import render

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
	





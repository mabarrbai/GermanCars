from django.test import TestCase
#from rest_framework import status
#from rest_framework.test import APITestCase
from penhas.models import Penha,Jugador

class PenhaTestCase(TestCase):
	def setUp(self):
		Penha.objects.create(nombre="El Tercer Tiempo", ciudad="Granada", direccion="Recogidas 1, Granada, Spain")
		Penha.objects.create(nombre="La Maceta", ciudad="Peligros",direccion="Av. Pechuelos 1, Peligros, Granada, Spain")

	def test_penhas_ciudad(self):
		"""Las ciudades de las penhas son correctas"""
		pMaceta = Penha.objects.get(nombre="La Maceta")
		pTercerTiempo = Penha.objects.get(nombre="El Tercer Tiempo")

		self.assertEqual(pMaceta.ciudad, 'Peligros')
		self.assertEqual(pMaceta.direccion, 'Av. Pechuelos 1, Peligros, Granada, Spain')
		self.assertEqual(pTercerTiempo.ciudad, 'Granada')
		self.assertEqual(pTercerTiempo.direccion, 'Recogidas 1, Granada, Spain')
		print("Test de creacion de penha correcto y superado.")

class JugadorTestCase(TestCase):
	def setUp(self):
		pTercerTiempo = Penha(nombre="El Tercer Tiempo", ciudad="Granada", direccion="Recogidas 1, Granada, Spain")
		pTercerTiempo.save()
		pMaceta = Penha(nombre="La Maceta", ciudad="Peligros",direccion="Av. Pechuelos 1, Peligros, Granada, Spain")
		pMaceta.save()
		Jugador.objects.create(nombre="Andres", apellidos="Iniesta", penha=pMaceta)
		Jugador.objects.create(nombre="Cristiano", apellidos="Biraghi", penha=pTercerTiempo)

	def test_jugador_pertenece_penha(self):
		"""Un jugador pertenece a una penha"""
		Iniesta = Jugador.objects.get(nombre="Andres", apellidos="Iniesta")
		Biraghi = Jugador.objects.get(nombre="Cristiano", apellidos="Biraghi")
		
		pMaceta = Penha.objects.get(nombre="La Maceta")
		pTercerTiempo = Penha.objects.get(nombre="El Tercer Tiempo")

		self.assertEqual(Iniesta.penha, pMaceta)
		self.assertEqual(Biraghi.penha, pTercerTiempo)
		print("Test de creacion de jugador y pertenencia a penha correcto y superado.")
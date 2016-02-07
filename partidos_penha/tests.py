from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from partidos_penha.models import Penha,Jugador

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

class RutasPenhasJSON(APITestCase):
	def test_listar_penhas(self):
		"""Listar todas las penhas en JSON"""
		Penha.objects.create(nombre="El Tercer Tiempo", ciudad="Granada")
		Penha.objects.create(nombre="La Maceta", ciudad="Peligros")

		response = self.client.get('json/penhas/')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response['Content-Type'], 'application/json')

		print("Ruta '/penhas/' consultada correctamente")

	def test_detalle_penha(self):
		"""Testea el listado de cada penha individualmente en JSON"""
		Penha.objects.create(nombre="El Tercer Tiempo", ciudad="Granada")
		Penha.objects.create(nombre="La Maceta", ciudad="Peligros")
		
		penhas = Penha.objects.values_list('id',flat=True)
		for i in penhas:
			response = self.client.get('json/penhas/'+str(i)+'/')
			self.assertEqual(response.status_code, status.HTTP_200_OK)
			self.assertEqual(response['Content-Type'], 'application/json')
			print("Ruta /penhas/" + str(i) + "/ consultada correctamente")
		
		print("Rutas de cada penha consultada correctamente")
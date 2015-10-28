from django.test import TestCase

from penhas.models import Penha,Jugador

class PenhaTestCase(TestCase):
	def setUp(self):
		Penha.objects.create(nombre="El Tercer Tiempo", ciudad="Granada")
		Penha.objects.create(nombre="La Maceta", ciudad="Peligros")

	def test_penhas_ciudad(self):
		"""Las ciudades de las penhas son correctas"""
		pMaceta = Penha.objects.get(nombre="La Maceta")
		pTercerTiempo = Penha.objects.get(nombre="El Tercer Tiempo")

		self.assertEqual(pMaceta.ciudad, 'Peligros')
		self.assertEqual(pTercerTiempo.ciudad, 'Granada')
		print("Test de creación de peña correcto y superado.")

class JugadorTestCase(TestCase):
	def setUp(self):
		pTercerTiempo = Penha(nombre="El Tercer Tiempo", ciudad="Granada")
		pTercerTiempo.save()
		pMaceta = Penha(nombre="La Maceta", ciudad="Peligros")
		pMaceta.save()
		Jugador.objects.create(nombre="Andres", apellidos="Iniesta", penha=pMaceta)
		Jugador.objects.create(nombre="Cristiano", apellidos="Biraghi", penha=pTercerTiempo)

	def test_jugador_pertenece_penha(self):
		"""Un jugador pertenece a una peña"""
		Iniesta = Jugador.objects.get(nombre="Andres", apellidos="Iniesta")
		Biraghi = Jugador.objects.get(nombre="Cristiano", apellidos="Biraghi")
		
		pMaceta = Penha.objects.get(nombre="La Maceta")
		pTercerTiempo = Penha.objects.get(nombre="El Tercer Tiempo")

		self.assertEqual(Iniesta.penha, pMaceta)
		self.assertEqual(Biraghi.penha, pTercerTiempo)
		print("Test de creación de jugador y pertenencia a peña correcto y superado.")
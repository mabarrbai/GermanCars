from django.db import models

class Penha(models.Model):
	nombre = models.CharField(max_length=30)
	ciudad = models.CharField(max_length=30)

	class Meta:
		ordering = ["nombre"]

	def __str__(self):
		return '%s de %s' %(self.nombre, self.ciudad)

class Jugador(models.Model):
	nombre = models.CharField(max_length=40)
	apellidos = models.CharField(max_length=50)
	penha = models.ForeignKey(Penha)

	class Meta:
		ordering = ["penha"]
	
	def __str__(self):
		return '%s %s' %(self.nombre, self.apellidos)

	
	

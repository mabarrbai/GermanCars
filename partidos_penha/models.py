from django.db import models

from django.template.defaultfilters import slugify

class Penha(models.Model):
	nombre = models.CharField(max_length=30)
	ciudad = models.CharField(max_length=30)
	visitas = models.IntegerField(default=0, editable = False)
	direccion = models.CharField(max_length=70)
	slug = models.SlugField(unique=True,default='')

	def save(self, *args, **kwargs):
                self.slug = slugify(self.nombre)
                super(Penha, self).save(*args, **kwargs)

	class Meta:
		ordering = ["nombre"]

	def __unicode__(self):
		return '%s de %s' %(self.nombre, self.ciudad)

class Jugador(models.Model):
	nombre = models.CharField(max_length=40)
	apellidos = models.CharField(max_length=50)
	penha = models.ForeignKey(Penha)
	megusta = models.IntegerField(default=0, editable=False)
	slug = models.SlugField(unique=True,default='')

	def save(self, *args, **kwargs):
                self.slug = slugify(self.penha.nombre+self.nombre+self.apellidos)
                super(Jugador, self).save(*args, **kwargs)

	class Meta:
		ordering = ["penha"]
	
	def __unicode__(self):
		return '%s %s' %(self.nombre, self.apellidos)

from django.db import models

# Create your models here.
class Service(models.Model):
	title    = models.CharField(max_length=200, verbose_name='Título')	
	subtitle = models.CharField(max_length=200, verbose_name='Subtítulo')
	content  = models.TextField(verbose_name='Contenido')
	image    = models.ImageField(upload_to="services", verbose_name='Imagen')
	created  = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
	updated  = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

	class Meta:
		verbose_name='Servicio'
		verbose_name_plural = 'Servicios' #Default agrega 's' al final
		ordering = ['-created']

	def __str__(self):
		return self.title



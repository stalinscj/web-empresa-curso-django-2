from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name    = models.CharField(max_length=100, verbose_name='Nombre')	
	created  = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
	updated  = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

	class Meta:
		verbose_name='categoría'
		verbose_name_plural = 'categorías' #Default agrega 's' al final
		ordering = ['name']

	def __str__(self):
		return self.name

class Post(models.Model):
	title      = models.CharField(max_length=200, verbose_name='Título')	
	content    = models.TextField(verbose_name='Contenido')
	published  = models.DateTimeField(verbose_name='Fecha de Publicación', default=now)
	image      = models.ImageField(upload_to="blog", verbose_name='Imagen', null=True, blank=True)
	author     = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
	categories = models.ManyToManyField(Category, verbose_name='Categorías', related_name="get_post") # Si no se agrega related name se accedería "categories.post_set"
	created    = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
	updated    = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

	class Meta:
		verbose_name='entrada'
		verbose_name_plural = 'entradas' #Default agrega 's' al final
		ordering = ['-created']

	def __str__(self):
		return self.title

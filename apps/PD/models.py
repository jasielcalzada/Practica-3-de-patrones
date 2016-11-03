from django.db import models

# Create your models here.
class resetas(models.Model):
	nombre = models.CharField(max_length=64,primary_key=True)
	def __unicode__(self):
		return '%s'%(self.nombre,)

class ingredientes(models.Model):
	reseta = models.ForeignKey(resetas)
	ingrediente = models.CharField(max_length=64)

	def __unicode__(self):
		return '%s %s'%(self.reseta,self.ingrediente)



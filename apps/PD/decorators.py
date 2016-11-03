from functools import wraps
from django.core.exceptions import PermissionDenied
from .models import resetas,ingredientes
from django.http import HttpResponse

ingrediente = 0
def entry_ingredientes(function):
	def wrap(request, *args, **kwargs):
		ingredient = ingredientes.objects.filter( int(ingrediente)).count()

		if ingredient.ingrediente >= 0:
			return function(request, *args, **kwargs)
		else:
			return HttpResponse("esta reseta no tiene ingredientes.")
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap





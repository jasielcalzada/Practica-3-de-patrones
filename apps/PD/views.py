from django.shortcuts import render
from django.views.generic import FormView, CreateView
from .models import resetas,ingredientes
from django.core.urlresolvers import reverse_lazy
from .decorators import entry_ingredientes
# Create your views here.

@entry_ingredientes
def index_view(request):
	return render(request,"PD/index.html")

class add_reseta(CreateView):
	template_name = 'PD/reseta.html'
	model = resetas
	fields = ['nombre']
	success_url = reverse_lazy('index_view')

	def get_context_data(self, **kwargs):
	 	ctx = super(add_reseta,self).get_context_data(**kwargs)
	 	ctx['reseta'] = ingredientes.objects.all()
	 	return ctx


class add_ingrediente(CreateView):
	template_name = 'PD/ingrediente.html'
	model = ingredientes
	fields = ['reseta','ingrediente']
	success_url = reverse_lazy('index_view')

	def get_context_data(self, **kwargs):
		ctx = super(add_ingrediente,self).get_context_data(**kwargs)
		ctx['resetas'] = resetas.objects.all()
		return ctx





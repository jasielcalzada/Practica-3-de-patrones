from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$',index_view,name = 'index_view'),
	url(r'^add_reseta/$',add_reseta.as_view(),name='add_reseta'),
	url(r'^add_ingrediente/$',add_ingrediente.as_view(),name='add_ingrediente'),
]
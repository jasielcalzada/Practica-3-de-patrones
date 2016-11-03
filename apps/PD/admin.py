from django.contrib import admin
from .models import resetas,ingredientes
# Register your models here.

@admin.register(resetas)
class resetas_admin(admin.ModelAdmin):
	list_display = ('nombre',)

@admin.register(ingredientes)
class ingredientes_admin(admin.ModelAdmin):
	list_display = ('id','reseta','ingrediente')


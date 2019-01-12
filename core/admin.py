from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Diretoria)
class DiretoriaAdmin(admin.ModelAdmin):
	list_display = ('cadastro','preco',)
	search_fields = ('cadastro',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
	list_display = ('comprar', 'quanty')
	search_fields = ('comprar',)
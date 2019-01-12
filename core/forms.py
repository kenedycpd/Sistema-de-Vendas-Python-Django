from django.forms import ModelForm
from .models import Diretoria, Pedido
class DiretoriaForm(ModelForm):
	class Meta:
		model = Diretoria
		fields = '__all__'

class PedidoForm(ModelForm):
	class Meta:
		model = Pedido
		fields = '__all__'
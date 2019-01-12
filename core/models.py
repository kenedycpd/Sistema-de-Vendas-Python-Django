from django.db import models

# Create your models here.
class Diretoria(models.Model):
	id = models.AutoField(primary_key=True)
	cadastro = models.CharField('Descrição do Produto', max_length=100, blank=False)
	preco = models.DecimalField('Preço do Produto', max_digits=10, decimal_places=3, blank=False)
	def __str__(self):
		return "%s" % self.cadastro

class Pedido(models.Model):
	id = models.AutoField(primary_key=True)
	comprar = models.ForeignKey(Diretoria, on_delete=models.CASCADE, verbose_name='Selecionar Produto')
	quanty = models.IntegerField('Quantidade')
	def __str__(self):
		return "%s" % self.comprar
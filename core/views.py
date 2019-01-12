from django.shortcuts import render, redirect
from .models import Diretoria, Pedido
from .forms import DiretoriaForm, PedidoForm
# Create your views here.
def home(request):
	return render(request, 'index.html')

def cadastro(request):
	if request.method == 'POST':
		form = DiretoriaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = DiretoriaForm()
	return render(request, 'core/cadastro.html',{'form':form})

def pedido(request):
	if request.method == 'POST':
		form = PedidoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('pedido')
	else:
		form = PedidoForm()
	return render(request, 'core/pedido.html',{'form':form})

def lista(request):
	list = Pedido.objects.all()
	return render(request, 'core/list.html',{'list':list})
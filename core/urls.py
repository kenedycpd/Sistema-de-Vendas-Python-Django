from django.urls import include, path
from . import views
urlpatterns = [
path('pedido/', views.pedido, name='pedido'),
path('cadastro/', views.cadastro, name='cadastro'),
path('lista', views.lista, name='lista'),

]
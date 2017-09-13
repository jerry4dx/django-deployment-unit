from django.shortcuts import render
from .models import Categoria, Contenido, SubCategoria
# Create your views here.

def index(request):
    return render(request, 'roberts/index.html')

def categorias(request):
    categorias = Categoria.objects.order_by('date_added')
    context = {'categorias': categorias}
    return render(request, 'roberts/categorias.html', context)

def categoria(request, categoria_id):
    """Muestra una sola categoria y sus subcategorias"""
    categoria = Categoria.objects.get(id=categoria_id)
    subcategorias = categoria.subcategoria_set.order_by('-date_added')
    context = {'categoria': categoria, 'subcategorias': subcategorias}
    return render(request, 'roberts/categoria.html', context)

def contenido(request, subcategoria_id):
    """Muestra 1 sola subcategoria y sus contenidos"""
    subcategoria = SubCategoria.objects.get(id=subcategoria_id)
    contenido = Contenido.objects.order_by('-date_added')
    context ={'contenido':contenido, 'subcategoria':subcategoria}
    return  render(request, 'roberts/contenido.html', context)

#def subcategoria(request):
 #   subcategoria =
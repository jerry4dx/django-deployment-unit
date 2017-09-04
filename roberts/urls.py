from django.conf.urls import url

from . import views

urlpatterns = [
    # HOME
    url(r'^$', views.index, name='index'),
    url(r'^categorias/$', views.categorias, name = 'categorias'),
    url(r'^categoria/(?P<categoria_id>\d+)/$', views.categoria, name = 'categoria'),
   # url(r'^subcategoria/(?P<subcategoria_id>\d+)/$', views.subcategoria, name = 'subcategoria'),
]
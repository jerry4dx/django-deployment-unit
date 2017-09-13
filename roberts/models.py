from django.db import models

from django.contrib import admin

# Create your models here.
class Categoria(models.Model):
    """Las categorias"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devuelve una representacion del modelo en formato string"""
        return self.text

class SubCategoria(models.Model):
    """Sub-Categorias"""
    categoria = models.ForeignKey(Categoria)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Sub-Categorias'

    def __str__(self):
        return '%s %s' % (self.text, self.categoria)

class Contenido(models.Model):
    """Aqui van los procesos"""
    subcategoria = models.ForeignKey(SubCategoria)
    titulo = models.CharField(max_length=130)
    descripcion = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'contenidos'


    def __str__(self):
        return '%s %s' % (self.titulo, self.subcategoria)

class ContentAdmin(admin.ModelAdmin):
    list_display = ('subcategoria', 'titulo', 'date_added')

admin.site.register(Contenido, ContentAdmin)
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")


    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["-created"] # Ordena los proyectos en base a la fecha de creación de cada uno. El "-" representa que se ordena de mas nuevo a mas viejo.

    def __str__(self):
        return self.name # Nos devuelve ahora el nombre del proyecto en el apartado de Django.
    
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de Publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog",null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE) # delete on Cascade
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"] # Ordena los proyectos en base a la fecha de creación de cada uno. El "-" representa que se ordena de mas nuevo a mas viejo.

    def __str__(self):
        return self.title # Nos devuelve ahora el nombre del proyecto en el apartado de Django.
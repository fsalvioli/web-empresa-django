from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    substitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to='services', verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["-created"] # Ordena los proyectos en base a la fecha de creación de cada uno. El "-" representa que se ordena de mas nuevo a mas viejo.

    def __str__(self):
        return self.title # Nos devuelve ahora el nombre del proyecto en el apartado de Django.
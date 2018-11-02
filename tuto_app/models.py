from django.db import models


class Categoria(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=30)


class Producto(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL)

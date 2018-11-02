from rest_framework import serializers
from tuto_app.models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'codigo','descripcion')
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id','codigo', 'categoria')
        
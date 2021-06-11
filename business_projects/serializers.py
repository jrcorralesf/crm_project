from rest_framework import serializers

from .models import ProductModel, SupplyModel
from .utils import ArrayOfCodesSerializer, ArrayOfNumberSerializer

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=ProductModel
        fields=['code','name','cost','stock']

class SupplySerializer(serializers.ModelSerializer):
    #products=ProductSerializer(many=True) #para ver los detalles en el listado
    #prods=ArrayOfCodesSerializer(required=False) #para recibir la lista de los pk de los productos
    #quantities=ArrayOfNumberSerializer(required=False) #para recibir la lista de las cantidades a sacar de cada producto

    class Meta:
        model=SupplyModel
        fields=['code','name','products']
        #fields=['code','name','products','prods','quantities']
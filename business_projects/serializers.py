from rest_framework import serializers

from .models import ProductModel, SupplyModel

class ProductSerializer(serializers.ModelSerializer):
    path = serializers.CharField(max_length=50, required=False)
    class Meta:
        model=ProductModel
        fields=['code','name','cost','stock','photo','path']

class SupplySerializer(serializers.ModelSerializer):
    #products=ProductSerializer(many=True) #para ver los detalles en el listado
    #prods=ArrayOfCodesSerializer(required=False) #para recibir la lista de los pk de los productos
    #quantities=ArrayOfNumberSerializer(required=False) #para recibir la lista de las cantidades a sacar de cada producto

    class Meta:
        model=SupplyModel
        fields=['code','name','products']
        #fields=['code','name','products','prods','quantities']
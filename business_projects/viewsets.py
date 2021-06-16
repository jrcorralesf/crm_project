from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser,AllowAny
from rest_framework.response import Response

from .serializers import ProductSerializer, SupplySerializer
from .models import ProductModel, SupplyModel
from .azure_files_services import upload_file

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    
    def create(self, request, *args, **kwargs): 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        #proceso para guardar el archivo subido dentro del Azure files
        photo_validated=serializer.validated_data['photo']
        upload_file(photo_validated)
        


        #alternativa para guardar ProductModel.objects.create()
        product=ProductModel(
            code = serializer.validated_data['code'],
            name = serializer.validated_data['name'],
            cost = serializer.validated_data['cost'],
            stock = serializer.validated_data['stock'],
            #photo= 'null' #PONER URL DE AZURE
        )
        product.save()

        return Response('Producto almacenado en Azure Files correctamente')
        #headers = self.get_success_headers(product)
        #return Response(product, status=status.HTTP_201_CREATED, headers=headers)

class SupplyViewSet(viewsets.ModelViewSet):
    queryset = SupplyModel.objects.all()
    serializer_class = SupplySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    #def list(self, request, *args, **kwargs):
    #   return Response('Crea un nuevo grupo de insumos')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        selected_products=serializer.validated_data['products'] #recupera el listado de productos seleccionado
        for product in selected_products:
            product.stock -= 1
            product.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

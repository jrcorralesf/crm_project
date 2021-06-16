from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser,AllowAny
from rest_framework.response import Response

from .serializers import ProductSerializer, SupplySerializer
from .models import ProductModel, SupplyModel

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

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

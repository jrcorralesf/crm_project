from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser,AllowAny

from .serializers import RoleSerializer, UserSerializer
from .models import RoleModel, UserModel

class RoleViewSet(viewsets.ModelViewSet):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if (self.action=='create'):
            permission_classes=AllowAny
        else:
            permission_classes=IsAdminUser
        #return super().get_permissions(self)
        return [permission() for permission in self.permission_classes]
    

from django.contrib.auth.models import User
from rest_framework.routers import DefaultRouter

from .viewsets import RoleViewSet, UserRegistrationViewSet

router = DefaultRouter()

# En el router vamos añadiendo los endpoints a los viewsets
router.register(r'roles', RoleViewSet, basename='roles_viewset')
router.register(r'user/registratoon', UserRegistrationViewSet, basename='user_registration')

urlpatterns = router.urls
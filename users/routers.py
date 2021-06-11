

from rest_framework.routers import DefaultRouter

from .viewsets import RoleViewSet, UserRegistrationViewSet

router = DefaultRouter()

# En el router vamos añadiendo los endpoints a los viewsets
router.register(r'roles', RoleViewSet, basename='roles_router')
router.register(r'user/registration', UserRegistrationViewSet, basename='user_registration_router')

urlpatterns = router.urls
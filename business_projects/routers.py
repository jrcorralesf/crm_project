

from rest_framework.routers import DefaultRouter

from .viewsets import ProductViewSet, SupplyViewSet

router = DefaultRouter()

# En el router vamos añadiendo los endpoints a los viewsets
router.register(r'products', ProductViewSet, basename='product_router')
router.register(r'supplies', SupplyViewSet, basename='supply_router')

urlpatterns = router.urls
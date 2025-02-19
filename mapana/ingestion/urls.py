from rest_framework import routers
from .api import DepartmentViewSet, AisleViewSet, ProductViewSet, OrderViewSet, OrderProductViewSet

router = routers.DefaultRouter()

router.register('api/department', DepartmentViewSet, 'department')
router.register('api/aisle', AisleViewSet, 'aisle')
router.register('api/product', ProductViewSet, 'product')
router.register('api/order', OrderViewSet, 'order')
router.register('api/order_product', OrderProductViewSet, 'order_product')

urlpatterns = router.urls

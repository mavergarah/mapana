from .models import Department, Aisle, Product, Order, OrderProduct
from rest_framework import viewsets, permissions
from serializers import OrderSerializer, DepartmentSerializer, AisleSerializer, ProductSerializer, OrderProductSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DepartmentSerializer

class AisleViewSet(viewsets.ModelViewSet):
    queryset = Aisle.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AisleSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderSerializer

class OrderProductViewSet(viewsets.ModelViewSet):
    queryset = OrderProduct.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderProductSerializer

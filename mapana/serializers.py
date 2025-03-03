from rest_framework import serializers
from ingestion.models import Department, Aisle, Product, Order, OrderProduct

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('department_id', 'department')
        read_only_fields = ('department_id',)

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('order_id', 'user_id', 'eval_set', 'order_number',
        'order_dow', 'order_hour_of_day', 'days_since_prior_order'
        )
        read_only_fields = ('order_id','order_dow', 'order_hour_of_day', 'days_since_prior_order')

class AisleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aisle
        fields = ('aisle_id', 'aisle')
        read_only_fields = ('aisle',)

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('product_id', 'product_name', 'aisle_id', 'department_id')
        read_only_fields = ('product_id',)

class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderProduct
        fields = ('order_id', 'product_id', 'add_to_cart_order', 'reordered')
        read_only_fields = ('order_id',)

from django.db import models

# Create your models here.
class Department(models.Model):
    department_id = models.AutoField(
        primary_key=True
    )
    department = models.CharField(
        max_length=100,
        verbose_name='department',
        blank=False
    )

    def __str__(self):
        return self.department

class Aisle(models.Model):
    aisle_id = models.AutoField(
        primary_key=True
    )
    aisle = models.CharField(
        max_length=50,
        verbose_name='aisle',
        blank=False
    )

    def __str__(self):
        return self.aisle

class Product(models.Model):
    product_id = models.AutoField(
        primary_key=True
    )
    product_name = models.CharField(
        max_length=150,
        verbose_name='product_name',
        blank=False
    )

    aisle_id = models.ForeignKey(
        Aisle,
        on_delete=models.CASCADE
    )

    department_id = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.product_id

class Order(models.Model):
    order_id = models.IntegerField()
    user_id = models.IntegerField()
    eval_set = models.CharField(
        max_length=50,
        blank=False,
    )
    order_number = models.IntegerField()
    order_dow = models.IntegerField()
    order_hour_of_day = models.IntegerField()
    days_since_prior_order = models.IntegerField()

    def __str__(self):
        return self.order_id

class OrderProduct(models.Model):
    order_id = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    add_to_cart_order = models.IntegerField()
    reordered = models.IntegerField()

    def __str__(self):
        return self.order_id

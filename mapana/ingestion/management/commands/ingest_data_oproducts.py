import csv
from django.core.management.base import BaseCommand
from ingestion.models import Department, Product, Aisle, Order, OrderProduct

class Command(BaseCommand):
    help = 'Command for importing data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('order_product_csv', type=str, help='Path to the order products CSV file')

    def handle(self, *args, **options):
        csv_file = options['order_product_csv']
        max_rows = 500000
        row_count = 0

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row_count >= max_rows:
                    break

                try:
                    order_id_integer = int(row['order_id'])
                    product_id_integer = int(row['product_id'])

                    # This is for testing variables
                    print('Order ID Integer=%d' %order_id_integer)
                    print('Order ID Integer=%d' %product_id_integer)

                    # Since order_id is not primary_key it should be used filter
                    order_id_instance = Order.objects.get(order_id=order_id_integer)
                    product_id_instance = Product.objects.get(product_id=product_id_integer)

                    # This is for testing variables
                    print('Order ID Integer=%s' %order_id_instance)
                    print('Order ID Integer=%s' %product_id_instance)

                    model_instance = OrderProduct(
                        order_id = order_id_instance,
                        product_id = product_id_instance,
                        add_to_cart_order = row['add_to_cart_order'],
                        reordered = row['reordered']
                    )
                    print('Despues del Model_Instance')
                    model_instance.save()
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Successfully imported products"
                        )
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error importing row {e}"))

                row_count += 1

            self.stdout.write(self.style.SUCCESS(f"Data import completed"))

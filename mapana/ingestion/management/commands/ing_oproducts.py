from django.core.management.base import BaseCommand
from ingestion.models import Department, Product, Aisle, Order, OrderProduct
import pandas as pd

class Command(BaseCommand):
    help = 'Command for importing data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('order_products_csv', type=str, help='Path to the ORDER PRODUCTS CSV file')

    def handle(self, *args, **options):
        csv_file = options['order_products_csv']
        count = 0
        count_rows = 0

        df_oproducts = pd.read_csv(csv_file)

        for index, row in df_oproducts.iterrows():
            if count_rows >= 500000:
                break

            try:
                order_id_integer = int(row['order_id'])
                product_id_integer = int(row['product_id'])

                order_id_instance = Order.objects.get(order_id = order_id_integer)
                product_id_instance = Product.objects.get(product_id = product_id_integer)

                model_instance = OrderProduct(
                    order_id = order_id_instance,
                    product_id = product_id_instance,
                    add_to_cart_order = row['add_to_cart_order'],
                    reordered = row['reordered'],
                )
                model_instance.save()
                count += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error importing row {index + 1}: {e}."))

        self.stdout.write(self.style.SUCCESS(f"Data import completed. {count} record imported."))
        error_perc = (count_rows - count)*100 / count_rows
        print('El porcentaje de datos no cargados es: %f' %error_perc)

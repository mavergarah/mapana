from django.core.management.base import BaseCommand
from ingestion.models import Department, Product, Aisle, Order, OrderProduct
import pandas as pd

class Command(BaseCommand):
    help = 'Command for importing data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('order_csv', type=str, help='Path to the ORDER CSV file')

    def handle(self, *args, **options):
        csv_file = options['order_csv']
        count = 0
        count_rows = 0

        df_orders = pd.read_csv(csv_file)

        for index, row in df_orders.iterrows():
            if count_rows >= 100000:
                break
            try:
                model_instance = Order(
                    order_id = row['order_id'],
                    user_id = row['user_id'],
                    eval_set = row['eval_set'],
                    order_number = row['order_number'],
                    order_dow = row['order_dow'],
                    order_hour_of_day = row['order_hour_of_day'],
                    days_since_prior_order = int(float(row['days_since_prior_order'])),
                )
                model_instance.save()
                count += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error importing row {index + 1}: {e}."))
            count_rows += 1

        self.stdout.write(self.style.SUCCESS(f"Data import completed. {count} record imported."))
        error_perc = (count_rows - count)*100 / count_rows
        print('El porcentaje de datos no cargados es: %f' %error_perc)

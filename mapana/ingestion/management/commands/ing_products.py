from django.core.management.base import BaseCommand
from ingestion.models import Department, Product, Aisle, Order, OrderProduct
import pandas as pd

class Command(BaseCommand):
    help = 'Command for importing data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('product_csv', type=str, help='Path to the PRODUCT CSV file')

    def handle(self, *args, **options):
        csv_file = options['product_csv']
        count = 0

        df_products = pd.read_csv(csv_file)

        for index, row in df_products.iterrows():
            try:
                department_instance = Department.objects.get(department_id = row['department_id'])
                aisle_instance = Aisle.objects.get(aisle_id = row['aisle_id'])
                model_instance = Product(
                    product_name = row['product_name'],
                    department_id = department_instance,
                    aisle_id = aisle_instance
                )
                model_instance.save()
                count += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error importing row {index + 1}: {e}."))

        self.stdout.write(self.style.SUCCESS(f"Data import completed. {count} record imported."))

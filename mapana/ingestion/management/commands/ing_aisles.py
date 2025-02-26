from django.core.management.base import BaseCommand
from ingestion.models import Department, Product, Aisle, Order, OrderProduct
import pandas as pd

class Command(BaseCommand):
    help = 'Command for importing data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('aisle_csv', type=str, help='Path to the AISLE CSV file')

    def handle(self, *args, **options):
        csv_file = options['aisle_csv']
        count = 0

        df_aisles = pd.read_csv(csv_file)

        for index, row in df_aisles.iterrows():
            try:
                model_instance = Aisle(
                    aisle = row['aisle']
                )
                model_instance.save()
                count += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error importing row {index + 1}: {e}."))

        self.stdout.write(self.style.SUCCESS(f"Data import completed. {count} record imported."))

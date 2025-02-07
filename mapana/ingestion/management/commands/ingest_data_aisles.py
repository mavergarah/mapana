import csv
from django.core.management.base import BaseCommand
from ingestion.models import Department, Product, Aisle, Order, OrderProduct

class Command(BaseCommand):
    help = 'Command for importing data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('aisle_csv', type=str, help='Path to the aisle CSV file')

    def handle(self, *args, **options):
        csv_file = options['aisle_csv']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    model_instance = Aisle(
                        aisle = row['aisle']
                    )
                    model_instance.save()
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Successfully imported aisles"
                        )
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error importing row {e}"))

            self.stdout.write(self.style.SUCCESS(f"Data import completed"))

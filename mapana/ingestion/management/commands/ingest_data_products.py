import csv
from django.core.management.base import BaseCommand
from ingestion.models import Department, Product, Aisle, Order, OrderProduct

class Command(BaseCommand):
    help = 'Command for importing data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('products_csv', type=str, help='Path to the products CSV file')

    def handle(self, *args, **options):
        csv_file = options['products_csv']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    aisle_instance = Aisle.objects.get(aisle_id=int(row['aisle_id']))
                    department_instance = Department.objects.get(department_id=int(row['department_id']))
                    model_instance = Product(
                        product_name = row['product_name'],
                        aisle_id = aisle_instance,
                        department_id = department_instance
                    )
                    model_instance.save()
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Successfully imported products"
                        )
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error importing row {e}"))

            self.stdout.write(self.style.SUCCESS(f"Data import completed"))

import csv
from django.core.management.base import BaseCommand
from ingestion.models import Department, Product, Aisle, Order, OrderProduct

class Command(BaseCommand):
    help = 'Command for importing data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('order_csv', type=str, help='Path to the order CSV file')

    def handle(self, *args, **options):
        csv_file = options['order_csv']
        max_rows = 100000
        row_count = 0

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row_count >= max_rows:
                    break

                try:
                    user_id_instance = Department(row['user_id'])
                    model_instance = Order(
                        user_id = user_id_instance
                    )
                    model_instance.save()
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Successfully imported orders"
                        )
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error importing row {e}"))

                row_count += 1

            self.stdout.write(self.style.SUCCESS(f"Data import completed"))

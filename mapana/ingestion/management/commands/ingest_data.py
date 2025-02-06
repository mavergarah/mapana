import csv
from django.core.management.base import BaseCommand
from ingestion.models import Department, Product, Aisle, Order, OrderProduct

class Command(BaseCommand):
    help = 'Command for importing data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('departments_csv', type=str, help='Path to the departments CSV file')
        parser.add_argument('aisle_csv', type=str, help='Path to the products CSV file')
        parser.add_argument('products_csv', type=str, help='Path to the departments CSV file')
        parser.add_argument('order_product_csv', type=str, help='Path to the products CSV file')
        parser.add_argument('order_csv', type=str, help='Path to the products CSV file')

    def handle(self, *args, **options):
        csv_file = options['departments_csv']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    model_instance = Department(
                        department = row['department']
                    )
                    model_instance.save()
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Successfully imported department"
                        )
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error importing row {e}"))

            self.stdout.write(self.style.SUCCESS(f"Data import completed"))

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

    def handle(self, *args, **options):
        csv_file = options['products_csv']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    aisle_instance = Aisle.objects.get(pk=row['aisle_id'])
                    department_instance = Department.objects.get(pk=row['department_id'])
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
                    order_id_instance = Order.objects.get(pk=row['order_id'])
                    product_id_instance = Product.objects.get(pk=row['product_id'])
                    model_instance = OrderProduct(
                        order_id = order_id_instance,
                        product_id = product_id_instance,
                        aisle_id = row['aisle_id'],
                        department_id = row['department_id']
                    )
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
                    user_id_instance = Department.objects.get(pk=row['user_id'])
                    model_instance = Order(
                        order_id = row['order_id'],
                        user_id = user_id_instance,
                        eval_set = row['eval_set'],
                        order_number = row['order_number'],
                        order_dow = row['order_dow'],
                        order_hour_of_day = row['order_hour_of_day'],
                        days_since_prior_order = row['days_since_prior_order']
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

from django.core.management.base import BaseCommand
from django.apps import apps
from ingestion.models import Department, Product, Aisle, Order, OrderProduct
import json
from django.db import models
import pandas as pd

class Command(BaseCommand):
    help = 'Command for ingesting data from a CSV file.'

    def add_arguments(self, parser):
        parser.add_argument('JSON_file', type=str, help='Path to the JSON settings file')

    def handle(self, *args, **options):
        config_file = options['JSON_file']
        #print('Contenido de la variable config_file (options): %s' %config_file)

        # Load JSON file
        with open(config_file, 'r') as file:
            config = json.load(file)

        # Extract Data
        source_type = config['source']['type']
        source_path = config['source']['path']

        if source_type == 'csv':
            df = pd.read_csv(source_path)
        else:
            self.stdout.write(self.style.ERROR(f"Unsupported source type: {source_type}"))
            return

        # Transform data
        if 'transformations' in config:
            for transformation in config['transformations']:
                if transformation['type'] == 'map':
                    df[transformation['to']] = df[transformation['field']]
                elif transformation['type'] == 'lookup':
                    # Obtener el modelo de búsqueda
                    lookup_model = apps.get_model('ingestion', transformation['lookup_source'])
                    # Crear un diccionario para mapear valores a IDs
                    lookup_dict = {
                        getattr(obj, transformation['lookup_field']): obj.pk
                        for obj in lookup_model.objects.all()
                    }
                    # Aplicar la búsqueda
                    df[transformation['to']] = df[transformation['field']].map(lookup_dict)
                else:
                    self.stdout.write(self.style.ERROR(f"Unsupported transformation type: {transformation['type']}"))

        # Load data in Django models
        app_model = config['destination']['model']
        field_mapping = config['destination']['field_mapping']

        app, model = app_model.split('.')
        Model = apps.get_model(app, model)
        #print('app es: %s y model es: %s' %(app, model))

        # Create and save objects
        count = 0

        for index, row in df.iterrows():
            data = {}
            for source_field, field in field_mapping.items():
                if field.endswith('_id') and isinstance(Model._meta.get_field(field), models.ForeignKey):
                    related_model_name = field.replace('_id','')
                    try:
                        related_model = apps.get_model('ingestion', related_model_name.capitalize())
                        filter_kwargs = {field: int(row[source_field])}
                        data[field] = related_model.objects.get(**filter_kwargs)
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f"Skipping row {index + 1}: {related_model_name} ID {row[source_field]} not found. {e}"))
                        continue
                else:
                    data[field] = row[source_field]
            try:
                Model.objects.create(**data)
                count += 1
            except Exception as e:
                if config['error_handling']['strategy'] == 'skip_row':
                    self.stdout.write(self.style.WARNING(f"Skipping row {index + 1}: {e}"))
                else:
                    self.stdout.write(self.style.ERROR(f"Error importing row {index + 1}: {e}"))
                    return
        self.stdout.write(self.style.SUCCESS(f"ETL process completed. {count} records imported."))

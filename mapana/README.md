# 1. Mamba Project: Data Ingestion with Django and PostgreSQL
Is a project for ingesting data which uses Django and PostgresQL

# 2. Requirements
* Python 3.9
* Django 4.1
* psycopg2-binary

# 3. Installation
## 3.1. Clone Respository
  '''
  git clone
  '''

## 3.2. Create a Virtual Environment
  '''
  conda create --name mapana_env
  '''

## 3.3. Activate the Virtual Environment
  '''
  conda activate mapana_env
  '''

## 3.4. Install Dependencies
  '''
  pip install -r requirements.txt
  '''

## 3.5. Set Database

If you want to run this project in your local machine
in setting.py file set the database of the project to:

  '''
  DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'mi_proyecto_django',
                'USER': 'tu_usuario_de_postgres',
                'PASSWORD': 'tu_contraseña_de_postgres',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }
  '''

If you want to deploy this project use a .env file to protect
the data base information from hack actions. Change your settings.py
file as:

  '''
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME':     os.environ.get('POSTGRES_DB',       ''),
          'USER':     os.environ.get('POSTGRES_USER',     ''),
          'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
          'HOST': 'postgres',
          'PORT': '5432',
      }
  }
  '''

## 3.5. Run Migrations

  '''
  python manage.py migrate
  '''

## 3.6. Run Server

  '''
  python manage.py runserver
  '''

## 3.7. Go to Your Web Browser

  '''
  http://127.0.0.1:8000/
  '''

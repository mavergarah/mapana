FROM python:3.9-alpine3.20

# Add requirements to the image.
ADD requirements.txt /app/requirements.txt

# Asign work directory.
WORKDIR /app/

# Install Python requirements.
RUN pip install --upgrade pip; \
    pip cache purge; \
    pip install -r requirements.txt

# Create user without privilegies.
RUN adduser --disabled-password --gecos '' app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

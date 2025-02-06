from django.db import models

# Create your models here.
class Department(models.Model):
    department_id = models.AutoField(
        primary_key=True
    )
    department = models.CharField(
        max_length=50,
        verbose_name='department',
        blank=False,
        unique=True
    )

    def __str__(self):
        return self.department

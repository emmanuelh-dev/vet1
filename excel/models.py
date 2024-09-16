from django.db import models

# Create your models here.
# models.py
from django.db import models

class Covid19Record(models.Model):
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    symptoms = models.TextField()
    diagnosis_date = models.DateField()
    is_recovered = models.BooleanField(default=False)

    def __str__(self):
        return self.patient_name

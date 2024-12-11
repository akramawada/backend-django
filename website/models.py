from django.db import models
from django.contrib.auth.models import User


# from django.contrib.auth import authenticate

# from .views import username

# Create your models here.

###############################################


class Record(models.Model):
    company_name = models.CharField(max_length=100)
    service_required = models.CharField(max_length=500)
    date_start = models.DateField()
    status = models.CharField(max_length=12)
    completion_date = models.DateField(default='12/05/2025')

    createdBy = models.CharField(max_length=30,default=None)

    def __str__(self):
        return self.company_name
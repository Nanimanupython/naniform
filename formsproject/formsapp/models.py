from django.db import models

class FormsData(models.Model):
    first_name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=25)
    salary = models.IntegerField()
    address = models.CharField(max_length=25)

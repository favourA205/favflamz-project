from django.db import models

# Create your models here.
class RegistrationData(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.CharField(max_length=200)
    Phone_number = models.CharField(max_length=200)

    def __str__(self):
        return self.First_name



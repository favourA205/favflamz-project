from django.db import models

# Create your models here.
class RegistrationData(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    Email = models.CharField(max_length=200)
    Phone_number = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.username)



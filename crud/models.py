from django.db import models

# Create your models here.

class Employees(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name
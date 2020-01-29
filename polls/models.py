from django.db import models


# Create your models here.

class BabySitter(models.Model):
	Name = models.CharField(max_length=200)
	Email = models.EmailField(max_length=254) 
	DateOfBirth = models.DateField()



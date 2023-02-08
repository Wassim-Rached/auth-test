from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	content = models.TextField(max_length=255, blank=True, null=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

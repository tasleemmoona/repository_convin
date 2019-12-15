from django.db import models

# Create your models here.
class mytable_test(models.Model):
	char = models.CharField(max_length=200)
	file = models.FileField()
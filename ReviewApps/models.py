from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Issue(models.Model):
	type=models.CharField(max_length=100)
	room=models.CharField(max_length=100)
	details=models.TextField()
	date_submitted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(slef):
		return self.type


class Product(models.Model):
	name = models.CharField(default = '', max_length = 255)
	brand = models.CharField(default = '', max_length = 255)
	category = models.CharField(default = '', max_length = 255)
	date_released = models.DateField(default = timezone.now)
	description = models.TextField()

	def __str__(self):
		return self.name

class Review(models.Model):
	author = models.ForeignKey(User, on_delete= models.CASCADE)
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	rating = models.IntegerField(default = 0, max_length = 5)
	review_text = models.TextField()
	Date = models.DateField(default = timezone.now)
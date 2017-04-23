from django.db import models	

class Post(models.Model):
	"""docstring for Post"""
	title=models.CharField()
	body=models.TextField()
	date=models.DateTimeField()

	def __str__(self):
		return self.title

		

from django.db import models

# Create your models here.

class Question(models.Model):
	text = models.TextField()
	active = models.BooleanField(default=True)
	draft = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self): #def __str__(self):
		return self.text[:10]
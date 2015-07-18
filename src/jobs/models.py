from django.conf import settings
from django.db import models
from localflavor.us.models import USStateField
# Create your models here.

User = settings.AUTH_USER_MODEL

class Job(models.Model):
	text = models.CharField(max_length=120)
	active = models.BooleanField(default=True) #shown
	flagged = models.ManyToManyField(User, null=True, blank=True) #warning
	#users = modeles.ManyToManyField(User, null=True, blank=True)

	def __unicode__(self):
		return self.text




class Location(models.Model):
	name = models.CharField(max_length=250)
	active = models.BooleanField(default=True) #shown
	flagged = models.ManyToManyField(User, null=True, blank=True) 
 
	def __unicode__(self): #__str__(self):
		return self.name




class Employer(models.Model):
	name =  models.CharField(max_length=250)
	location = models.ForeignKey(Location, null=True, blank=True)
	#state = USStateField(null=True, blank=True)
	#website
	#lat_lang

	def __unicode__(self):
		return self.name
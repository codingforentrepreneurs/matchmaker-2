from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify


from localflavor.us.models import USStateField
# Create your models here.

User = settings.AUTH_USER_MODEL

class Job(models.Model):
	text = models.CharField(max_length=120, unique=True)
	slug = models.SlugField()
	active = models.BooleanField(default=True) #shown
	flagged = models.ManyToManyField(User, blank=True) #warning
	#users = modeles.ManyToManyField(User, null=True, blank=True)

	def __unicode__(self):
		return self.text

def pre_save_job(sender, instance, *args, **kwargs):
	instance.slug = slugify(instance.text)
pre_save.connect(pre_save_job, sender=Job)



class Location(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField()
	active = models.BooleanField(default=True) #shown
	flagged = models.ManyToManyField(User, blank=True) 
 
	def __unicode__(self): #__str__(self):
		return self.name

def pre_save_location(sender, instance, *args, **kwargs):
	instance.slug = slugify(instance.name)
pre_save.connect(pre_save_location, sender=Location)


class Employer(models.Model):
	name =  models.CharField(max_length=250)
	slug = models.SlugField()
	location = models.ForeignKey(Location, null=True, blank=True) # is _city
	#city = mode
	#state = USStateField(null=True, blank=True)
	#website
	#lat_lang

	def __unicode__(self):
		return self.name


def pre_save_employer(sender, instance, *args, **kwargs):
	instance.slug = slugify(instance.name)
pre_save.connect(pre_save_employer, sender=Employer)









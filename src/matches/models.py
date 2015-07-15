from django.conf import settings
from django.db import models

# Create your models here.


class Match(models.Model):
	user_a = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='match_user_a')
	user_b = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='match_user_b')
	match_decimal = models.DecimalField(decimal_places=8, max_digits=16, default=0.00)
	questions_answered = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #__str__(self)
		return self.match_decimal

	#good match?
	#percentage value?
	
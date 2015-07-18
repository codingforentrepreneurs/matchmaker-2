import datetime
from decimal import Decimal

from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
from .utils import get_match


class MatchQuerySet(models.query.QuerySet):
	def all(self):
		return self.filter(active=True)

	def matches(self, user):
		q1 = self.filter(user_a = user)
		q2 = self.filter(user_b = user)
		return (q1 | q2).distinct()



class MatchManager(models.Manager):
	def get_queryset(self):
		return MatchQuerySet(self.model, using=self._db)


	def get_or_create_match(self, user_a=None, user_b=None):
		try:
			obj = self.get(user_a=user_a, user_b=user_b)
		except:
			obj = None
		try:
			obj_2 = self.get(user_a=user_b, user_b=user_a)
		except:
			obj_2 = None
		if obj and not obj_2:
			obj.check_update()
			return obj, False
		elif not obj and obj_2:
			obj_2.check_update()
			return obj_2, False
		else:
			new_instance = self.create(user_a=user_a, user_b=user_b)
			new_instance.do_match()
			return new_instance, True

	def update_all(self):
		queryset = self.all()
		now = timezone.now()
		offset = now - datetime.timedelta(hours=12)
		offset2 = now - datetime.timedelta(hours=36)
		queryset.filter(updated__gt=offset2).filter(updated__lte=offset)
		if queryset.count > 0:
			for i in queryset:
				i.check_update()
			
	def matches_all(self, user):
		return self.get_queryset().matches(user)


class Match(models.Model):
	user_a = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='match_user_a')
	user_b 	= models.ForeignKey(settings.AUTH_USER_MODEL, related_name='match_user_b')
	match_decimal = models.DecimalField(decimal_places=8, max_digits=16, default=0.00)
	questions_answered = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #__str__(self)
		return "%.2f" %(self.match_decimal)

	objects = MatchManager()

	#good match?
	#percentage value?
	@property
	def get_percent(self):
		new_decimal = self.match_decimal * Decimal(100)
		return  "%.2f%%" %(new_decimal)
	

	def do_match(self):
		user_a = self.user_a
		user_b = self.user_b
		match_decimal, questions_answered = get_match(user_a, user_b)
		self.match_decimal = match_decimal
		self.questions_answered = questions_answered
		self.save()
	
	def check_update(self):
		now = timezone.now()
		offset = now - datetime.timedelta(hours=12)  # 12 hours ago
		if self.updated <= offset or self.match_decimal == 0.0:
			self.do_match()
		else:
			print("already updated")



'''
Match.abc.get_or_create_match()
Match.objects.get_or_create_match()


Match.objects.all()
Match.objects.get(user_a=some_user)
instance, created = Match.objects.get_or_create(user_a=some_user)
new_instance = Match.objects.create(user_a=some_user)


new_instance = Match()
new_instance.user_a = some_user
new_instance.save()

'''
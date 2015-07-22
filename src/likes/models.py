from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL


class UserLikeManager(models.Manager):
	def get_all_mutual_likes(self, user, number):
		try:
			qs = user.liker.liked_users.all().order_by("?")
		except:
			return []
		mutual_users = [][:number]
		for other_user in qs:
			try:
				if other_user.liker.get_mutual_like(user):
					mutual_users.append(other_user)
			except:
				pass
		return mutual_users



class UserLike(models.Model):
	user = models.OneToOneField(User, related_name='liker')
	liked_users = models.ManyToManyField(User, related_name='liked_users', blank=True)

	objects = UserLikeManager()


	def __unicode__(self):
		return self.user.username

	def get_mutual_like(self, user_b):
		i_like = False
		you_like = False
		if user_b in self.liked_users.all():
			i_like = True
		liked_user, created = UserLike.objects.get_or_create(user=user_b)
		if self.user in liked_user.liked_users.all():
			you_like = True	
		if you_like and i_like:
			return True
		else:
			return False




#request.user.liker.liked_users.all()

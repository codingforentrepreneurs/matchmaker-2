from django.contrib.auth import get_user_model

from questions.models import UserAnswer


User = get_user_model()

users = User.objects.all() #[user1, user2,]
all_user_answers = UserAnswer.objects.all().order_by("user__id") #[useranswer1, useranswer2,]


jmitchel3 = users[0]
khaleesi = users[1]
userc = users[2]


UserAnswer.objects.filter(user=jmitchel3)


UserAnswer.objects.filter(user=khaleesi)


janswer1 = jmitchel3.useranswer_set.all()[0]
kanswer1 = khaleesi.useranswer_set.all()[0]


janswer1.question.id == kanswer1.question.id

j_answer = janswer1.my_answer


j_pref = janswer1.their_answer

k_answer = kanswer1.my_answer


k_pref = kanswer1.their_answer


j_answer == k_pref
j_pref == k_answer


def get_match(user_a, user_b):
	user_a_answers = UserAnswer.objects.filter(user=user_a)[0]
	user_b_answers = UserAnswer.objects.filter(user=user_b)[0]
	if user_a_answers.question.id == user_b_answers.question.id:
		user_a_answer = user_a_answers.my_answer
		user_a_pref = user_a_answers.their_answer
		user_b_answer = user_b_answers.my_answer
		user_b_pref = user_b_answers.their_answer
		user_a_total_awarded = 0
		user_b_total_awarded = 0
		if user_a_answer == user_b_pref:
			user_b_total_awarded += user_b_answers.their_points
			print "%s fits with %s's preference" %(user_a_answers.user.username, user_b_answers.user.username)
		if user_a_pref == user_b_answer:
			user_a_total_awarded += user_a_answers.their_points
			print "%s fits with %s's preference" %(user_a_answers.user.username, user_b_answers.user.username)
		if user_a_answer == user_b_pref and user_a_pref == user_b_answer:
			print "this is an ideal answer for both"
		print user_a, user_a_total_awarded, user_b
		print user_b, user_b_total_awarded, user_a




get_match(jmitchel3, khaleesi)
get_match(jmitchel3, userc)
get_match(khaleesi, userc)





def get_points(user_a, user_b):
	a_answers = UserAnswer.objects.filter(user=user_a)[0]
	b_answers = UserAnswer.objects.filter(user=user_b)[0]
	a_total_awarded = 0
	a_points_possible = 0
	if a_answers.question.id == b_answers.question.id:
		a_pref = a_answers.their_answer
		b_answer = b_answers.my_answer
		if a_pref == b_answer:
			'''
			awards points for correct answer
			'''
			a_total_awarded += a_answers.their_points
		'''
		assiging total points
		'''
		a_points_possible += a_answers.their_points
	print "%s has awarded %s points of %s to %s" %(user_a, a_total_awarded, a_points_possible, user_b)




# get_points(jmitchel3, khaleesi)
# get_points(jmitchel3, userc)
get_points(khaleesi, userc)
get_points(userc, khaleesi)










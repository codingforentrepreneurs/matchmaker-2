from decimal import Decimal
from django.contrib.auth import get_user_model
from django.db.models import Q
from questions.models import UserAnswer, Question


# User = get_user_model()

# users = User.objects.all() #[user1, user2,]
# all_user_answers = UserAnswer.objects.all().order_by("user__id") #[useranswer1, useranswer2,]


# jmitchel3 = users[0]
# khaleesi = users[1]
# userc = users[2]


def get_points_2(user_a, user_b):
	q1 = Q(useranswer__user=a)
	q2 = Q(useranswer__user=b)
	question_set = Question.objects.filter(q1 | q2).distinct()
	for question in question_set:
		try:
			a_answer = UserAnswer.objects.get(user=user_a, question=question)
		except:
			a_answer = None
		try:
			b_answer = UserAnswer.objects.get(user=user_b, question=question)
		except:
			b_answer = None
		if a_answer and b_answer:
			print("something")





def get_points(user_a, user_b):
	a_answers = UserAnswer.objects.filter(user=user_a)
	b_answers = UserAnswer.objects.filter(user=user_b)
	a_total_awarded = 0
	a_points_possible = 0
	num_question = 0
	for a in a_answers:
		for b in b_answers:
			if a.question.id == b.question.id:
				num_question += 1
				a_pref = a.their_answer
				b_answer = b.my_answer
				if a_pref == b_answer:
					'''
					awards points for correct answer
					'''
					a_total_awarded += a.their_points
				'''
				assiging total points
				'''
				a_points_possible += a.their_points
			print "%s has awarded %s points of %s to %s" %(user_a, a_total_awarded, a_points_possible, user_b)
	percent = a_total_awarded / Decimal(a_points_possible)
	print percent, num_question
	if percent == 0:
		percent = 0.000001
	return percent, num_question



# get_points(jmitchel3, khaleesi)
# # get_points(jmitchel3, userc)
# a = get_points(khaleesi, jmitchel3)
# b = get_points(jmitchel3, khaleesi)


# match_percentage = "%.2f" % ((Decimal(a[0]) * Decimal(b[0])) ** (1/Decimal(b[1])))
# print match_percentage

def get_match(user_a, user_b):
	a = get_points(user_a, user_b)
	b = get_points(user_b, user_a)
	#a[0] = decimal match value 
	number_of_questions = b[1] #b[1]/a[1] = number of questions answered
	match_decimal = (Decimal(a[0]) * Decimal(b[0])) ** (1/Decimal(number_of_questions)) #geometric mean in respects to number of questions answered
	return match_decimal, number_of_questions















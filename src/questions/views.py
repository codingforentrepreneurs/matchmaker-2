from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from matches.signals import user_matches_update

from .forms import UserResponseForm
from .models import Question, Answer, UserAnswer



def single(request, id):
	if request.user.is_authenticated():

		queryset = Question.objects.all().order_by('-timestamp')
		instance = get_object_or_404(Question, id=id)
		
		try:
			user_answer = UserAnswer.objects.get(user=request.user, question=instance)
			updated_q = True
		except UserAnswer.DoesNotExist:
			user_answer = UserAnswer()
			updated_q = False
		except UserAnswer.MultipleObjectsReturned:
			user_answer = UserAnswer.objects.filter(user=request.user, question=instance)[0]
			updated_q = True
		except:
			user_answer = UserAnswer()
			updated_q = False

		form = UserResponseForm(request.POST or None)
		if form.is_valid():
			print form.cleaned_data
			#print request.POST

			question_id = form.cleaned_data.get('question_id') #form.cleaned_data['question_id']
			
			answer_id = form.cleaned_data.get('answer_id')
			importance_level = form.cleaned_data.get('importance_level')

			their_importance_level = form.cleaned_data.get('their_importance_level')
			their_answer_id = form.cleaned_data.get('their_answer_id')

			
			question_instance = Question.objects.get(id=question_id)
			answer_instance = Answer.objects.get(id=answer_id)
			
			
			user_answer.user = request.user
			user_answer.question = question_instance
			user_answer.my_answer = answer_instance
			user_answer.my_answer_importance = importance_level
			if their_answer_id != -1:
				their_answer_istance = Answer.objects.get(id=their_answer_id)
				user_answer.their_answer = their_answer_istance
				user_answer.their_importance = their_importance_level
			else:
				user_answer.their_answer = None
				user_answer.their_importance = "Not Important"
			user_answer.save()

			user_matches_update.send(user=request.user, sender=user_answer.__class__)


			if updated_q:
				messages.success(request, "Your response was updated successfully.<br/><a href='#'>Hello</a>", extra_tags='safe updated')

			else:
				messages.success(request, "Your response was saved successfully.")


			next_q = Question.objects.get_unanswered(request.user).order_by("?")
			if next_q.count() > 0:
				next_q_instance = next_q.first()
				return redirect("question_single", id=next_q_instance.id)
			else:
				return redirect("home")

		context = {
			"form": form,
			"instance": instance,
			"user_answer": user_answer,
			#"queryset": queryset
		}
		return render(request, "questions/single.html", context)
	else:
		raise Http404



def home(request):
	if request.user.is_authenticated():
		form = UserResponseForm(request.POST or None)
		if form.is_valid():
			question_id = form.cleaned_data.get('question_id') #form.cleaned_data['question_id']
			answer_id = form.cleaned_data.get('answer_id')
			question_instance = Question.objects.get(id=question_id)
			answer_instance = Answer.objects.get(id=answer_id)
			print answer_instance.text, question_instance.text

		queryset = Question.objects.all().order_by('-timestamp')
		instance = queryset[1]
		context = {
			"form": form,
			"instance": instance,
			#"queryset": queryset
		}
		return render(request, "questions/home.html", context)
	else:
		raise Http404
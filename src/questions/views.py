from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from .forms import UserResponseForm
from .models import Question, Answer, UserAnswer



def single(request, id):
	if request.user.is_authenticated():
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
			
			new_user_answer = UserAnswer()
			new_user_answer.user = request.user
			new_user_answer.question = question_instance
			new_user_answer.my_answer = answer_instance
			new_user_answer.my_answer_importance = importance_level
			if their_answer_id != -1:
				their_answer_istance = Answer.objects.get(id=their_answer_id)
				new_user_answer.their_answer = their_answer_istance
				new_user_answer.their_importance = their_importance_level
			else:
				new_user_answer.their_importance = "Not Important"
			new_user_answer.save()

			next_q = Question.objects.all().order_by("?").first()
			return redirect("question_single", id=next_q.id)


		queryset = Question.objects.all().order_by('-timestamp')
		instance = get_object_or_404(Question, id=id)
		context = {
			"form": form,
			"instance": instance,
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
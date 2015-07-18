from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render


from matches.models import Match
from questions.models import Question

from .forms import ContactForm, SignUpForm
from .models import SignUp

# Create your views here.
def home(request):
	title = 'Sign Up Now'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}



	if form.is_valid():
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		context = {
			"title": "Thank you"
		}

	if request.user.is_authenticated():
		matches = []
		match_set = Match.objects.matches_all(request.user).order_by('-match_decimal')
		print match_set
		for match in match_set:
			if match.user_a == request.user and match.user_b != request.user:
				items_wanted = [match.user_b, match.get_percent]
				matches.append(items_wanted)
			elif match.user_b == request.user and match.user_a != request.user:
				items_wanted = [match.user_a, match.get_percent]
				matches.append(items_wanted)
			else:
				pass


		queryset = Question.objects.all().order_by('-timestamp') 
		context = {
			"queryset": queryset,
			"matches": matches[:6]
		}
		return render(request, "questions/home.html", context)

	return render(request, "home.html", context)



def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		# 	#print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email, message, full_name
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'youotheremail@email.com']
		contact_message = "%s: %s via %s"%( 
				form_full_name, 
				form_message, 
				form_email)
		some_html_message = """
		<h1>hello</h1>
		"""
		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				html_message=some_html_message,
				fail_silently=True)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}
	return render(request, "forms.html", context)

















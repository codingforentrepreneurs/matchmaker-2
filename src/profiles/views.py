from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.

User = get_user_model()

from matches.models import Match
from .forms import UserJobForm
from .models import Profile, UserJob

@login_required
def profile_view(request, username):
	user = get_object_or_404(User, username=username)
	profile, created = Profile.objects.get_or_create(user=user)
	match, match_created = Match.objects.get_or_create_match(user_a=request.user, user_b=user)
	jobs = user.userjob_set.all()
	context = {
		"profile": profile,
		"match": match,
		"jobs": jobs,
				}
	return render(request, "profiles/profile_view.html", context)



@login_required
def job_add(request):
	title = "Add Job"
	job = UserJob.objects.all()[0]
	form = UserJobForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
	context = {
		"form": form,
		"title": title,
				}
	return render(request, "forms.html", context)


@login_required
def jobs_edit(request):
	title = "Edit Jobs"
	UserJobFormset = modelformset_factory(UserJob, form=UserJobForm)
	queryset = UserJob.objects.filter(user=request.user)
	formset = UserJobFormset(request.POST or None, queryset=queryset)
	if formset.is_valid():
		instances = formset.save(commit=False)
		for instance in instances:
			instance.user = request.user
			instance.save()
	context = {
		"formset": formset,
		"title": title,
				}
	return render(request, "formset.html", context)











from django.shortcuts import render

# Create your views here.
from jobs.models import Job, Employer, Location

def position_match_view(request, slug):
	instance = Job.objects.get(slug=slug)
	template = "matches/position_match_view.html"
	context = {
		"instance": instance,
	}
	return render(request, template, context)
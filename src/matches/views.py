from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from jobs.models import Job, Employer, Location

def position_match_view(request, slug):
	try:
		instance = Job.objects.get(slug=slug)
	except Job.MultipleObjectsReturned:
		queryset = Job.objects.filter(slug=slug).order_by('-id')
		instance = queryset[0]
	except Job.DoesNotExist:
		raise Http404

	template = "matches/position_match_view.html"
	context = {
		"instance": instance,
	}
	return render(request, template, context)
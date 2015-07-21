from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from jobs.models import Job, Employer, Location

from .models import PositionMatch, LocationMatch, EmployerMatch

def position_match_view(request, slug):
	try:
		instance = Job.objects.get(slug=slug)
	except Job.MultipleObjectsReturned:
		queryset = Job.objects.filter(slug=slug).order_by('-id')
		instance = queryset[0]
	except Job.DoesNotExist:
		raise Http404

	matches = PositionMatch.objects.filter(job__text__iexact=instance.text)

	template = "matches/position_match_view.html"
	context = {
		"instance": instance,
		"matches": matches
	}
	return render(request, template, context)


def employer_match_view(request, slug):
	try:
		instance = Employer.objects.get(slug=slug)
	except Employer.MultipleObjectsReturned:
		queryset = Employer.objects.filter(slug=slug).order_by('-id')
		instance = queryset[0]
	except Employer.DoesNotExist:
		raise Http404

	template = "matches/employer_match_view.html"
	context = {
		"instance": instance,
	}
	return render(request, template, context)


def location_match_view(request, slug):
	try:
		instance = Location.objects.get(slug=slug)
	except Location.MultipleObjectsReturned:
		queryset = Location.objects.filter(slug=slug).order_by('-id')
		instance = queryset[0]
	except Location.DoesNotExist:
		raise Http404

	template = "matches/location_match_view.html"
	context = {
		"instance": instance,
	}
	return render(request, template, context)
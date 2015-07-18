from django.contrib import admin

# Register your models here.
from .models import Employer, Job, Location


admin.site.register(Job)
admin.site.register(Location)
admin.site.register(Employer)
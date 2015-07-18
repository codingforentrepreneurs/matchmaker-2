from django.contrib import admin

# Register your models here.

from .models import Profile, UserJob

admin.site.register(Profile)

admin.site.register(UserJob)
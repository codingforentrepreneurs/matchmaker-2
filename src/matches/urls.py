from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^position/(?P<slug>[\w-]+)/$', 'matches.views.position_match_view', name='position_match_view_url'),
]


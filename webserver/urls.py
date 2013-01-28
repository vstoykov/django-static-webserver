from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns('',
	url(r'^%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'),
		'django.views.static.serve',
		{'document_root': settings.STATIC_ROOT}),
	url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
		'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT}),
    url(r'^(?P<path>.*)$', 'webserver.views.render_template'),
)

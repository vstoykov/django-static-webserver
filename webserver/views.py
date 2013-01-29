from django.shortcuts import render, redirect, Http404
from django.template import TemplateDoesNotExist
from django.conf import settings


def render_template(request, path):
	if path and settings.APPEND_SLASH and not path.endswith('/'):
		return redirect('/%s/' % path)
	templates = [
			'%s.html' % path.rstrip('/'),
			'%sindex.html' % path
			]
	try:
		return render(request, templates, {'request': request})
	except TemplateDoesNotExist:
		raise Http404('/%s can not be found' % path)
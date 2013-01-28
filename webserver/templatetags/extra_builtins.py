from django.template import Library

register = Library()


@register.filter
def split(val, splitter):
	return val.split(splitter)
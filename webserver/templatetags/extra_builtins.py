from django.template import Library

register = Library()


@register.filter
def split(val, splitter):
	return val.split(splitter)


@register.filter
def replace(val, args):
	search_string, replacement = args.split(',')
	return val.replace(search_string, replacement)

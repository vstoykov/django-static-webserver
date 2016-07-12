"""
Add some filters to the builtins
"""
from django.template import defaultfilters


@defaultfilters.register.filter
def split(val, splitter):
    return val.split(splitter)


@defaultfilters.register.filter
def replace(val, args):
    search_string, replacement = args.split(',')
    return val.replace(search_string, replacement)

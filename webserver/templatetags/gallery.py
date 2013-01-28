import os
import posixpath

from django.template import Library
from django.core.files.storage import default_storage

register = Library()

IMAGE_EXTENSTIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff']


@register.inclusion_tag("_gallery.html")
def show_gallery(path, template="_gallery.html"):
	images = []
	for file_name in default_storage.listdir(path)[1]:
		name, ext = os.path.splitext(file_name)
		if ext in IMAGE_EXTENSTIONS:
			file_path = posixpath.join(path, file_name)
			images.append({
				'title': name,
				'url': default_storage.url(file_path)
			})
	return {'image_list': images, 'template': template}

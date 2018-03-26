import os
import io
from PIL import Image

from django.template import Library
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import File


register = Library()


def get_thumbnail_path(path, size):
    name, ext = os.path.splitext(path)
    return "thumbs/%s.%s%s" % (name, size, ext)


def create_thumbnail(_file, size, path):
    image = Image.open(_file)
    image.thumbnail(size, Image.ANTIALIAS)
    thumb = File(io.BytesIO(), name=path)
    image.save(thumb, image.format)
    thumb.size = len(thumb.file.getvalue())  # to use default_storage.save file must have size
    default_storage.save(path, thumb)
    return image


@register.filter
def as_thumbnail(image_path, size="100x100"):
    if image_path.startswith(default_storage.base_url):
        image_path = image_path[len(default_storage.base_url):]
    image = default_storage.open(image_path)

    thumb_path = get_thumbnail_path(image_path, size)

    if not default_storage.exists(thumb_path):
        size = map(int, size.split('x'))
        create_thumbnail(image, size, thumb_path)

    return default_storage.url(thumb_path)

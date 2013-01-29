django-static-webserver
=======================

This is a simple django server that serve static files and render simple templates based on entered url


Purpose
-------

The purpose of this project is to help front end coder to learn how to write simple django templates and also for rapid prototyping


How to use
--------------

First of all for start using django-static-webserver you must download it using git

    git clone git://github.com/vstoykov/django-static-webserver.git


or as ZIP package from https://github.com/vstoykov/django-static-webserver/archive/master.zip

Next you must you must create some folders and files. Directory tree must look like this:

    django-static-webserver\
                           |-- html\
                           |    |-- index.html
                           |
                           |-- static\
                           |-- media\
                           |-- webserver\
                           |-- manage.py


Contents in `static` directory are served as `/static/` and `media` is `/media/`. Every developer deside where to put his static files (javascript, style sheet and images) but if you want to use `as_thumbnail` (I will describe it later) images must be in media directory.

Contents in `html` directory are django templates. File structure in this directory describe possible urls. For example if you have template named `about.html` it can be opened at `/about/`, `contacts.html` will be `/contacts/` and etc.

If you want to make sub paths like `/about/company/` you can create directory `about` with file `company.html` in it. 

There is one more possible way to set urls based on file structure. Like clasical web servers if we have index.html file in a directory there is no need to explisitly type it. Url `/about/` can work if you have template `about/index.html`. This means that for root url `/` you can use only index.html file in html directory.

Template tags and filters
-------------------------

For easy creation of simple templates that can be functional I've made some template tags and filters.

**split** template filter. Implements the Python default split method to strings. This template filter is added to builtins. Usage:
  
    {% for item in "first,second,third"|split:"," %}
      do some thing
    {% endfor %}


**as_thumbnail** template filter. Use PIL to create a thumbnail for given image. Usage:

    {% load thumbnail %}
  
    <img src="{{ "/media/my_picture.jpg"|as_thumbnail:"100x100" }}">


only "my_pictre.jpg" can be used instead of "/media/my_picture.jpg" but `my_picture.jpg` must be in `media` directory.


**show_gallery** template tag. This tag accept relative path in media direcotry and try to browse for images. If this tag find images then create link to it with thumbnail of it for every image. Example:

    {% load gallery %}

    <div class="my-gallery">
      {% show_gallery "my_pictures" %}
    </div>


Final words
-----------

This project is in alpha stage but feel free to test it and if you have any suggestions you can tell me.

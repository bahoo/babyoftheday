{{ project_name }}
==================

A daily baby photo blog thing created in Django.

Just run:

    django-admin.py startproject --template=https://github.com/bahoo/babyoftheday/zipball/master yourbabyname
    cd yourbabyname
    chmod u+x manage.py
    ./manage.py personalize
    ./manage.py runserver

TODO
----
 - Better 404/etc templates
 - Better deploy / multi-environment story.
## {{ project_name }}

A daily baby photo blog thing created in Django.

Just run:

    django-admin.py startproject --template=https://github.com/bahoo/babyoftheday/zipball/master yourbabyname
    cd yourbabyname
    chmod u+x manage.py
    ./manage.py syncdb
    ./manage.py runserver
   
Not 100% functional just yet :D but close. Pull requests welcome.

### TODO
Figure out S3 / Boto
Optionally create S3 bucket if it doesn't already exist (see Cactus)
Better 404/etc templates
Keep ripping Max of the Day out
Better handle orientation on photos during upload
from django.shortcuts import render_to_response
from photos.models import *
# from django.contrib import messages
# from django.template import RequestContext
# from django.http import HttpResponseRedirect
# from twitter_app.views import tweet_photo


def home(request, *args, **kwargs):
    photo_list = Photo.objects.all()[0:9]
    return render_to_response('photos/home.html', {'photo_list': photo_list})

"""
def get_cookied(request, *args, **kwargs):

    next = request.POST.get('next', '/')

    if request.method == 'POST':
        if request.POST.get('password', '') == PASSWORD:
            request.session['password'] = request.POST.get('password')
            request.session.set_exiry(15778463)
            return HttpResponseRedirect(next)

        else:
            messages.add_message(request, messages.ERROR, "You've entered a password, but it's not correct.")

    return render_to_response('getcookied.html', {'next': next}, context_instance=RequestContext(request))
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import *
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404

from django.contrib import messages

from django.contrib.auth.decorators import login_required

def home(request):
    return render_to_response("upload_form.html",context_instance=RequestContext(request))

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import *
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from autograde.models import *
from autograde.forms import *

def home(request):
    form = ProjectForm()
    if request.method=="POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render_to_response("upload_form.html",{"form":form},context_instance=RequestContext(request))

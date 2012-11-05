from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import *
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404

from django.contrib.auth.decorators import login_required

from autograde.models import *
from autograde.forms import *

def project_create(request,
        form_class=ProjectCreateForm,
        template_name="autograde/project_create.html"):
    form = form_class()
    if request.method=="POST":
        form = form_class(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            project = form.instance
            return HttpResponseRedirect(project.get_absolute_url())
    return render_to_response(template_name,{"form":form},context_instance=RequestContext(request))

def testcase_delete(request,pk):
    tc = get_object_or_404(TestCase,pk=pk)
    tc.delete()
    return HttpResponse("Deleted")
def testcase_create(request,pk,
        form_class=TestCaseForm,
        template_name="autograde/testcase_edit.html"):
    project = get_object_or_404(Project,pk=pk)
    form = form_class()
    if request.method=="POST":
        form = form_class(request.POST,request.FILES)
        form.instance.project = project
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("project_detail",args=(project.pk,)))
    return render_to_response(template_name,{"form":form},context_instance=RequestContext(request))
def testcase_edit(request,pk,
        form_class=TestCaseForm,
        template_name="autograde/testcase_edit.html"):
    tc = get_object_or_404(TestCase,pk=pk)
    form = form_class(instance=tc)
    if request.method=="POST":
        form = form_class(request.POST,request.FILES,instance=tc)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("testcase_detail",args=(tc.pk,)))
    return render_to_response(template_name,{"form":form},context_instance=RequestContext(request))

def projectfile_delete(request,pk):
    pf = get_object_or_404(ProjectFile,pk=pk)
    pf.delete()
    return HttpResponse("Deleted")
def projectfile_create(request,pk,
        form_class=ProjectFileForm,
        template_name="autograde/projectfile_edit.html"):
    project = get_object_or_404(Project,pk=pk)
    form = form_class()
    if request.method=="POST":
        form = form_class(request.POST,request.FILES)
        form.instance.project = project
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("project_detail",args=(project.pk,)))
    return render_to_response(template_name,{"form":form},context_instance=RequestContext(request))
def projectfile_edit(request,pk,
        form_class=ProjectFileForm,
        template_name="autograde/projectfile_edit.html"):
    pf = get_object_or_404(ProjectFile,pk=pk)
    form = form_class(instance=pf)
    if request.method=="POST":
        form = form_class(request.POST,request.FILES,instance=pf)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("projectfile_detail",args=(pf.pk,)))
    return render_to_response(template_name,{"form":form},context_instance=RequestContext(request))


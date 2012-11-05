from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import *
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404

from django.contrib.auth.decorators import login_required

from autograde.models import *
from autograde.forms import *

def project_create(request):
    form = ProjectCreateForm()
    if request.method=="POST":
        form = ProjectCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            project = form.instance
            return HttpResponseRedirect(project.get_absolute_url())
    return render_to_response("autograde/project_create.html",{"form":form},context_instance=RequestContext(request))

def testcase_delete(request,pk):
    tc = get_object_or_404(TestCase,pk=pk)
    tc.delete()
    return HttpResponse("Deleted")
def testcase_create(request,pk):
    project = get_object_or_404(Project,pk=pk)
    form = TestCaseForm()
    if request.method=="POST":
        form = TestCaseForm(request.POST,request.FILES)
        form.instance.project = project
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("project_detail",args=(project.pk,)))
    return render_to_response("autograde/testcase_edit.html",{"form":form},context_instance=RequestContext(request))
def testcase_edit(request,pk):
    tc = get_object_or_404(TestCase,pk=pk)
    form = TestCaseForm(instance=tc)
    if request.method=="POST":
        form = TestCaseForm(request.POST,request.FILES,instance=tc)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("testcase_detail",args=(tc.pk,)))
    return render_to_response("autograde/testcase_edit.html",{"form":form},context_instance=RequestContext(request))

def projectfile_delete(request,pk):
    pf = get_object_or_404(ProjectFile,pk=pk)
    pf.delete()
    return HttpResponse("Deleted")
def projectfile_create(request,pk):
    project = get_object_or_404(Project,pk=pk)
    form = ProjectFileForm()
    if request.method=="POST":
        form = ProjectFileForm(request.POST,request.FILES)
        form.instance.project = project
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("project_detail",args=(project.pk,)))
    return render_to_response("autograde/projectfile_edit.html",{"form":form},context_instance=RequestContext(request))
def projectfile_edit(request,pk):
    pf = get_object_or_404(ProjectFile,pk=pk)
    form = ProjectFileForm(instance=pf)
    if request.method=="POST":
        form = ProjectFileForm(request.POST,request.FILES,instance=pf)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("projectfile_detail",args=(pf.pk,)))
    return render_to_response("autograde/projectfile_edit.html",{"form":form},context_instance=RequestContext(request))


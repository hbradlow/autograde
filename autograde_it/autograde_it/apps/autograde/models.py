from django.db import models
from django.db.models import permalink

from django.contrib.auth.models import User
# Create your models here.

from tastypie.models import create_api_key
models.signals.post_save.connect(create_api_key, sender=User)

class Project(models.Model):
    instructors = models.ManyToManyField(User)
    title = models.CharField(max_length=100)
    def __unicode__(self):
        return self.title
    @permalink
    def get_absolute_url(self):
        return ("project_detail",[self.pk])

class ProjectFile(models.Model):
    project = models.ForeignKey(Project)
    file = models.FileField(upload_to="project_files")
    is_student_viewable = models.BooleanField(default=False)
    def __unicode__(self):
        return str(self.file)
    @permalink
    def get_absolute_url(self):
        return ("projectfile_detail",[self.pk])

class TestCase(models.Model):
    project = models.ForeignKey(Project)
    file = models.FileField(upload_to="tests")
    def __unicode__(self):
        return str(self.file)
    @permalink
    def get_absolute_url(self):
        return ("testcase_detail",[self.pk])

class TestResult(models.Model):
    test_case = models.ForeignKey(TestCase)
    results = models.TextField()
    user = models.ForeignKey(User)
    def __unicode__(self):
        print str(self.user) + ": " + self.results

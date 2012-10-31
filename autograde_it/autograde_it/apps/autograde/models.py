from django.db import models
from django.db.models import permalink

from django.contrib.auth.models import User
# Create your models here.

from tastypie.models import create_api_key
models.signals.post_save.connect(create_api_key, sender=User)


class KVPair(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    def __unicode__(self):
        return self.key + ": " + self.value

class Project(models.Model):
    instructor = models.ManyToManyField(User)
    zipped = models.FileField(upload_to="project_files")
    title = models.CharField(max_length=100)
    settings = models.ManyToManyField(KVPair,related_name="settings")
    @permalink
    def get_absolute_url(self):
        return ("project_detail",[self.pk])

class ProjectFile(models.Model):
    my_file = models.FileField(upload_to="project_files")
    is_student_viewable = models.BooleanField(default=False)
    project = models.ForeignKey(Project)
    def __unicode__(self):
        return str(self.my_file)

class TestCase(models.Model):
    file = models.FileField(upload_to="tests")
    project = models.ForeignKey(Project)
    def __unicode__(self):
        return str(self.my_file)

class Result(models.Model):
    text = models.TextField()

class Submission(models.Model):
    project = models.ForeignKey(Project)
    student = models.ForeignKey(User)
    files = models.ManyToManyField(ProjectFile,blank=True)
    results = models.ForeignKey(Result)
class TestResult(models.Model):
    test_case = models.ForeignKey(TestCase)
    results = models.TextField()
    user = models.ForeignKey(User)

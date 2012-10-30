from django.db import models
from django.db.models import permalink

from django.contrib.auth.models import User
# Create your models here.

class TestCase(models.Model):
    my_file = models.FileField(upload_to="tests")
    def __unicode__(self):
        return str(self.my_file)

class ProjectFile(models.Model):
    my_file = models.FileField(upload_to="project_files")
    is_student_viewable = models.BooleanField(default=False)
    def __unicode__(self):
        return str(self.my_file)

class KVPair(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    def __unicode__(self):
        return self.key + ": " + self.value

class Project(models.Model):
    instructor = models.ManyToManyField(User)
    test_cases = models.ManyToManyField(TestCase)
    student_files = models.ManyToManyField(KVPair,related_name="student_files")
    framework_files = models.ManyToManyField(ProjectFile,related_name="framework_files")
    zipped = models.FileField(upload_to="project_files")
    title = models.CharField(max_length=100)
    verifier = models.ManyToManyField(ProjectFile,related_name="verifier")
    settings = models.ManyToManyField(KVPair,related_name="settings")
    @permalink
    def get_absolute_url(self):
        return ("project_detail",[self.pk])

class Result(models.Model):
    text = models.TextField()

class Submission(models.Model):
    project = models.ForeignKey(Project)
    student = models.ForeignKey(User)
    files = models.ManyToManyField(ProjectFile,blank=True)
    results = models.ForeignKey(Result)

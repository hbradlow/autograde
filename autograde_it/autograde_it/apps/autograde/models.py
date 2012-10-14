from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class TestCase(models.Model):
    file = models.FileField(upload_to="tests")

class ProjectFile(models.Model):
    file = models.FileField(upload_to="project_files")
    is_student_viewable = models.BooleanField(default=False)

class KVPair(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

class Project(models.Model):
    instructor = models.ManyToManyKey(User)
    test_cases = models.ManyToManyField(TestCase)
    student_files = models.ManyToManyField(KVPair)
    framework_files = models.ManyToManyField(ProjectFile)
    zipped = models.FileField()
    title = models.CharField(max_length=100)
    verifier = models.ManyToManyField(ProjectFile)
    settings = models.ManyToManyField(KVPair)

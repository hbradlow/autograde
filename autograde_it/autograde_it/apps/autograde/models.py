from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class TestCase(models.Model):
    file = models.FileField(upload_to="tests")
class ProjectFile(models.Model):
    file = models.FileField(upload_to="project_files")
    is_student_viewable = models.BooleanField(default=False)
class Project(models.Model):
    instructor = models.ForeignKey(User)
    test_cases = models.ManyToManyField(TestCase,blank=True)
    student_files = models.ManyToManyField(ProjectFile,blank=True)
class Result(models.Model):
    text = models.TextField()
class Submission(models.Model):
    project = models.ForeignKey(Project)
    student = models.ForeignKey(User)
    files = models.ManyToManyField(ProjectFile,blank=True)
    results = models.ForeignKey(Result)

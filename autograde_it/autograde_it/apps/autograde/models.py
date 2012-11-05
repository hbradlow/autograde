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
    expected_results = models.TextField(null=True)
    def __unicode__(self):
        return str(self.file)
    @permalink
    def get_absolute_url(self):
        return ("testcase_detail",[self.pk])

class TestResult(models.Model):
    test_case = models.ForeignKey(TestCase)
    results = models.TextField()
    user = models.ForeignKey(User)

    passed = models.BooleanField(default=False)
    was_checked = models.BooleanField(default=False)
    
    def check(self):
        """
            Check this test result against its test case.
        """
        if self.results == self.test_case.expected_results:
            self.passed = True
        else:
            self.passed = False
        self.was_checked = True
        self.save()

    def __unicode__(self):
        return str(self.user) + ": " + str(self.passed)
    @permalink
    def get_absolute_url(self):
        return ("testresult_detail",[self.pk])

def check_testresult(sender, instance, created, **kwargs):
    if created:
        instance.check()
models.signals.post_save.connect(check_testresult, sender=TestResult)

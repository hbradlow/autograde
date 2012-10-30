from django.contrib import admin
from autograde.models import *
admin.site.register(TestCase)
admin.site.register(ProjectFile)
admin.site.register(Project)
admin.site.register(KVPair)
admin.site.register(Result)
admin.site.register(Submission)
admin.site.register(TestResult)

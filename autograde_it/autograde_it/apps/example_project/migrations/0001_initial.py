# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserFeedback'
        db.create_table('example_project_userfeedback', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ("Please first create a project using the 'Create Project' button on the homepage. If this process is confusing, or could otherwise be improved, please let us know:", self.gf('django.db.models.fields.TextField')()),
            ('After creating the project, please upload a few project files and test files for the project. The project files will be included in the zip file that the students download, and the test files will be used to test the project. Each test file should have some expected results that indicate what the response of the output of the test case should be for a successful test. If this process is confusing, or could otherwise be improved, please let us know:', self.gf('django.db.models.fields.TextField')()),
            ("After the project has been created, click 'Get Zipped Files' on the project detail page to download the code. If this process is confusing, or could otherwise be improved, please let us know:", self.gf('django.db.models.fields.TextField')()),
            ('Please unzip the archive and run the python file in the base directory. It will ask you for your username and api_key in order to comunicate with the server. After running the test, you can check back to the project detail page to see the results of each of the test cases. If this process is confusing, or could otherwise be improved, please let us know:', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('example_project', ['UserFeedback'])


    def backwards(self, orm):
        # Deleting model 'UserFeedback'
        db.delete_table('example_project_userfeedback')


    models = {
        'example_project.userfeedback': {
            'After creating the project, please upload a few project files and test files for the project. The project files will be included in the zip file that the students download, and the test files will be used to test the project. Each test file should have some expected results that indicate what the response of the output of the test case should be for a successful test. If this process is confusing, or could otherwise be improved, please let us know:': ('django.db.models.fields.TextField', [], {}),
            "After the project has been created, click 'Get Zipped Files' on the project detail page to download the code. If this process is confusing, or could otherwise be improved, please let us know:": ('django.db.models.fields.TextField', [], {}),
            'Meta': {'object_name': 'UserFeedback'},
            "Please first create a project using the 'Create Project' button on the homepage. If this process is confusing, or could otherwise be improved, please let us know:": ('django.db.models.fields.TextField', [], {}),
            'Please unzip the archive and run the python file in the base directory. It will ask you for your username and api_key in order to comunicate with the server. After running the test, you can check back to the project detail page to see the results of each of the test cases. If this process is confusing, or could otherwise be improved, please let us know:': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['example_project']
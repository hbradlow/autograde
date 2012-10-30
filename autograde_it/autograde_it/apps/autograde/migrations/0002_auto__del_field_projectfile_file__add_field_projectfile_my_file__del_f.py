# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ProjectFile.file'
        db.delete_column('autograde_projectfile', 'file')

        # Adding field 'ProjectFile.my_file'
        db.add_column('autograde_projectfile', 'my_file',
                      self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100),
                      keep_default=False)

        # Deleting field 'TestCase.file'
        db.delete_column('autograde_testcase', 'file')

        # Adding field 'TestCase.my_file'
        db.add_column('autograde_testcase', 'my_file',
                      self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'ProjectFile.file'
        raise RuntimeError("Cannot reverse this migration. 'ProjectFile.file' and its values cannot be restored.")
        # Deleting field 'ProjectFile.my_file'
        db.delete_column('autograde_projectfile', 'my_file')

        # Adding field 'TestCase.file'
        db.add_column('autograde_testcase', 'file',
                      self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100),
                      keep_default=False)

        # Deleting field 'TestCase.my_file'
        db.delete_column('autograde_testcase', 'my_file')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'autograde.kvpair': {
            'Meta': {'object_name': 'KVPair'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'autograde.project': {
            'Meta': {'object_name': 'Project'},
            'framework_files': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'framework_files'", 'symmetrical': 'False', 'to': "orm['autograde.ProjectFile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'settings': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'settings'", 'symmetrical': 'False', 'to': "orm['autograde.KVPair']"}),
            'student_files': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'student_files'", 'symmetrical': 'False', 'to': "orm['autograde.KVPair']"}),
            'test_cases': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['autograde.TestCase']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'verifier': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'verifier'", 'symmetrical': 'False', 'to': "orm['autograde.ProjectFile']"}),
            'zipped': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'autograde.projectfile': {
            'Meta': {'object_name': 'ProjectFile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_student_viewable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'my_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'autograde.result': {
            'Meta': {'object_name': 'Result'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'autograde.submission': {
            'Meta': {'object_name': 'Submission'},
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['autograde.ProjectFile']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['autograde.Project']"}),
            'results': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['autograde.Result']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'autograde.testcase': {
            'Meta': {'object_name': 'TestCase'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'my_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['autograde']
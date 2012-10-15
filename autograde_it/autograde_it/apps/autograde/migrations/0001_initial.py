# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TestCase'
        db.create_table('autograde_testcase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('my_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('autograde', ['TestCase'])

        # Adding model 'ProjectFile'
        db.create_table('autograde_projectfile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('my_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('is_student_viewable', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('autograde', ['ProjectFile'])

        # Adding model 'KVPair'
        db.create_table('autograde_kvpair', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('autograde', ['KVPair'])

        # Adding model 'Project'
        db.create_table('autograde_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zipped', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('autograde', ['Project'])

        # Adding M2M table for field instructor on 'Project'
        db.create_table('autograde_project_instructor', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['autograde.project'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('autograde_project_instructor', ['project_id', 'user_id'])

        # Adding M2M table for field test_cases on 'Project'
        db.create_table('autograde_project_test_cases', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['autograde.project'], null=False)),
            ('testcase', models.ForeignKey(orm['autograde.testcase'], null=False))
        ))
        db.create_unique('autograde_project_test_cases', ['project_id', 'testcase_id'])

        # Adding M2M table for field student_files on 'Project'
        db.create_table('autograde_project_student_files', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['autograde.project'], null=False)),
            ('kvpair', models.ForeignKey(orm['autograde.kvpair'], null=False))
        ))
        db.create_unique('autograde_project_student_files', ['project_id', 'kvpair_id'])

        # Adding M2M table for field framework_files on 'Project'
        db.create_table('autograde_project_framework_files', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['autograde.project'], null=False)),
            ('projectfile', models.ForeignKey(orm['autograde.projectfile'], null=False))
        ))
        db.create_unique('autograde_project_framework_files', ['project_id', 'projectfile_id'])

        # Adding M2M table for field verifier on 'Project'
        db.create_table('autograde_project_verifier', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['autograde.project'], null=False)),
            ('projectfile', models.ForeignKey(orm['autograde.projectfile'], null=False))
        ))
        db.create_unique('autograde_project_verifier', ['project_id', 'projectfile_id'])

        # Adding M2M table for field settings on 'Project'
        db.create_table('autograde_project_settings', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['autograde.project'], null=False)),
            ('kvpair', models.ForeignKey(orm['autograde.kvpair'], null=False))
        ))
        db.create_unique('autograde_project_settings', ['project_id', 'kvpair_id'])

        # Adding model 'Result'
        db.create_table('autograde_result', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('autograde', ['Result'])

        # Adding model 'Submission'
        db.create_table('autograde_submission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['autograde.Project'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('results', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['autograde.Result'])),
        ))
        db.send_create_signal('autograde', ['Submission'])

        # Adding M2M table for field files on 'Submission'
        db.create_table('autograde_submission_files', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('submission', models.ForeignKey(orm['autograde.submission'], null=False)),
            ('projectfile', models.ForeignKey(orm['autograde.projectfile'], null=False))
        ))
        db.create_unique('autograde_submission_files', ['submission_id', 'projectfile_id'])


    def backwards(self, orm):
        # Deleting model 'TestCase'
        db.delete_table('autograde_testcase')

        # Deleting model 'ProjectFile'
        db.delete_table('autograde_projectfile')

        # Deleting model 'KVPair'
        db.delete_table('autograde_kvpair')

        # Deleting model 'Project'
        db.delete_table('autograde_project')

        # Removing M2M table for field instructor on 'Project'
        db.delete_table('autograde_project_instructor')

        # Removing M2M table for field test_cases on 'Project'
        db.delete_table('autograde_project_test_cases')

        # Removing M2M table for field student_files on 'Project'
        db.delete_table('autograde_project_student_files')

        # Removing M2M table for field framework_files on 'Project'
        db.delete_table('autograde_project_framework_files')

        # Removing M2M table for field verifier on 'Project'
        db.delete_table('autograde_project_verifier')

        # Removing M2M table for field settings on 'Project'
        db.delete_table('autograde_project_settings')

        # Deleting model 'Result'
        db.delete_table('autograde_result')

        # Deleting model 'Submission'
        db.delete_table('autograde_submission')

        # Removing M2M table for field files on 'Submission'
        db.delete_table('autograde_submission_files')


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
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_student_viewable': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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

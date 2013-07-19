# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Asset'
        db.create_table(u'base_asset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('continent', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2)),
        ))
        db.send_create_signal(u'base', ['Asset'])


    def backwards(self, orm):
        # Deleting model 'Asset'
        db.delete_table(u'base_asset')


    models = {
        u'base.asset': {
            'Meta': {'object_name': 'Asset'},
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['base']
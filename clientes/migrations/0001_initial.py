# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UF'
        db.create_table(u'clientes_uf', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sigla', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'clientes', ['UF'])

        # Adding model 'Cidade'
        db.create_table(u'clientes_cidade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uf', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.UF'])),
        ))
        db.send_create_signal(u'clientes', ['Cidade'])

        # Adding model 'Cliente'
        db.create_table(u'clientes_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cidade'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('obs', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'clientes', ['Cliente'])

        # Adding model 'Contato'
        db.create_table(u'clientes_contato', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('setor', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
        ))
        db.send_create_signal(u'clientes', ['Contato'])

        # Adding model 'Configuracao'
        db.create_table(u'clientes_configuracao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
            ('servidor', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('porta', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('endereco_web', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('arquivo_config', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'clientes', ['Configuracao'])


    def backwards(self, orm):
        # Deleting model 'UF'
        db.delete_table(u'clientes_uf')

        # Deleting model 'Cidade'
        db.delete_table(u'clientes_cidade')

        # Deleting model 'Cliente'
        db.delete_table(u'clientes_cliente')

        # Deleting model 'Contato'
        db.delete_table(u'clientes_contato')

        # Deleting model 'Configuracao'
        db.delete_table(u'clientes_configuracao')


    models = {
        u'clientes.cidade': {
            'Meta': {'object_name': 'Cidade'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.UF']"})
        },
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cidade']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'obs': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'clientes.configuracao': {
            'Meta': {'object_name': 'Configuracao'},
            'arquivo_config': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'endereco_web': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'porta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'servidor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'clientes.contato': {
            'Meta': {'object_name': 'Contato'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'setor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'clientes.uf': {
            'Meta': {'object_name': 'UF'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['clientes']
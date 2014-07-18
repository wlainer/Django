# -*- coding: utf-8 -*-

from django.db import models


class UF(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __unicode__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    uf = models.ForeignKey(UF)

    def __unicode__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255, null=True, blank=True)
    #  endereco = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.ForeignKey(Cidade)
    email = models.EmailField(null=True, blank=True)
    obs = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=255, null=True, blank=True)
    setor = models.CharField(max_length=255, null=True, blank=True)
    cliente = models.ForeignKey(Cliente)


class Configuracao(models.Model):
    descricao = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente)
    servidor = models.CharField(max_length=255, null=True, blank=True)
    porta = models.IntegerField(null=True, blank=True)
    endereco_web = models.CharField(max_length=255, null=True, blank=True)
    arquivo_config = models.FileField(upload_to='config', null=True, blank=True)

    def __unicode__(self):
        return "%s:%s" % (self.servidor, self.porta)

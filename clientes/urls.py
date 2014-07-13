# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from clientes import views

urlpatterns = patterns('',
## URL CRUD CLIENTE
  url(r'^$', views.cliente_list, name='cliente_list'),
  url(r'^new$', views.cliente_create, name='cliente_new'),
  url(r'^edit/(?P<pk>\d+)$', views.cliente_update, name='cliente_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.cliente_delete, name='cliente_delete'),
  
## URL CRUD CONTATO
  url(r'^(?P<pk>\d+)/contato/$', views.contato_list, name='contato_list'),
  url(r'^(?P<pk>\d+)/contato/new$', views.contato_create, name='contato_new'),
  url(r'^contato/edit/(?P<pk>\d+)$', views.contato_update, name='contato_edit'),
  url(r'^contato/delete/(?P<pk>\d+)$', views.contato_delete, name='contato_delete'),
  
## URL CRUD CONFIGURACAO
  url(r'^(?P<pk>\d+)/configuracao/$', views.configuracao_list, name='configuracao_list'),
  url(r'^(?P<pk>\d+)/configuracao/new$', views.configuracao_create, name='configuracao_new'),
  url(r'^configuracao/edit/(?P<pk>\d+)$', views.configuracao_update, name='configuracao_edit'),
  url(r'^configuracao/delete/(?P<pk>\d+)$', views.configuracao_delete, name='configuracao_delete'),

## URL CRUD ESTADO
  url(r'^uf/$', views.uf_list, name='uf_list'),
  url(r'^uf/new$', views.uf_create, name='uf_new'),
  url(r'^uf/edit/(?P<pk>\d+)$', views.uf_update, name='uf_edit'),
  url(r'^uf/delete/(?P<pk>\d+)$', views.uf_delete, name='uf_delete'),

## URL CRUD CIDADE
  url(r'^cidade/$', views.cidade_list, name='cidade_list'),
  url(r'^cidade/new$', views.cidade_create, name='cidade_new'),
  url(r'^cidade/edit/(?P<pk>\d+)$', views.cidade_update, name='cidade_edit'),
  url(r'^cidade/delete/(?P<pk>\d+)$', views.cidade_delete, name='cidade_delete'),
  
)
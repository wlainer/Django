# -*- coding: utf-8 -*-

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from django.core.urlresolvers import reverse

from clientes.models import Cidade, Cliente, Configuracao, Contato, UF

class UFForm(forms.ModelForm):
    class Meta:
        model = UF

class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade

class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Enviar'))
        self.helper.layout.append(Submit('cancel', 'Cancelar'))
    class Meta:
        model = Cliente

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ['cliente']

class ConfiguracaoForm(forms.ModelForm):
     def __init__(self, *args, **kwargs):
        super(ConfiguracaoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse('clientes:configuracao_new' , args=(1,))
        self.helper.layout.append(Submit('save', 'Enviar'))
        self.helper.layout.append(Submit('cancel', 'Cancelar'))
     class Meta:
        model = Configuracao
        exclude = ['cliente']

class PesquisaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PesquisaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Pesquisar'))
    pesquisar = forms.CharField(max_length=100)
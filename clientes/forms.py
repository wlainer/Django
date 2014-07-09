from django import forms

from clientes.models import Cidade, Cliente, Configuracao, Contato, UF

class UFForm(forms.ModelForm):
    class Meta:
        model = UF

class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato   
        exclude = ['cliente']                     

class ConfiguracaoForm(forms.ModelForm):
    class Meta:
        model = Configuracao
        exclude = ['cliente']

class PesquisaForm(forms.Form):
    pesquisar = forms.CharField(max_length=100)
# Create your views here.
from django.core.urlresolvers import reverse

from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from form_utils import forms

from clientes.models import UF, Cidade, Cliente, Configuracao, Contato


# ##################
# ## CRUD ESTADO
# ##################
class UFForm(forms.BetterModelForm):
    class Meta:
        model = UF


def uf_list(request):
    template_name = 'clientes/uf_list.jade'
    objects = UF.objects.all()
    data = {}
    data['object_list'] = objects
    return render(request, template_name, data)


def uf_create(request):
    template_name = 'clientes/form.jade'
    form = UFForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clientes:uf_list')
    return render(request, template_name, {'form': form})


def uf_update(request, pk):
    template_name = 'clientes/form.jade'
    object = get_object_or_404(UF, pk=pk)
    form = UFForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        return redirect('clientes:uf_list')
    return render(request, template_name, {'form': form})


def uf_delete(request, pk):
    template_name = 'clientes/confirm_delete.jade'
    object = get_object_or_404(UF, pk=pk)
    if request.method == 'POST':
        object.delete()
        return redirect('clientes:uf_list')
    return render(request, template_name, {'object': object})


###################
### CRUD CIDADE
###################    
class CidadeForm(forms.BetterModelForm):
    class Meta:
        model = Cidade


def cidade_list(request):
    template_name = 'clientes/cidade_list.jade'
    objects = Cidade.objects.all()
    data = {}
    data['object_list'] = objects
    return render(request, template_name, data)


def cidade_create(request):
    template_name = 'clientes/form.jade'
    form = CidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clientes:cidade_list')
    return render(request, template_name, {'form': form})


def cidade_update(request, pk):
    template_name = 'clientes/form.jade'
    object = get_object_or_404(Cidade, pk=pk)
    form = CidadeForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        return redirect('clientes:cidade_list')
    return render(request, template_name, {'form': form})


def cidade_delete(request, pk):
    template_name = 'clientes/confirm_delete.jade'
    object = get_object_or_404(Cidade, pk=pk)
    if request.method == 'POST':
        object.delete()
        return redirect('clientes:cidade_list')
    return render(request, template_name, {'object': object})


###################
### CRUD CLIENTE
###################    
class ClienteForm(forms.BetterModelForm):
    class Meta:
        model = Cliente
        fieldsets = [('Dados pessoais', {'fields': ['nome', 'telefone', 'cidade', 'email', 'obs', ],
                  #'description': 'Information',
                  'classes': ['Personal data']
        }),]


def cliente_list(request):
    template_name = 'clientes/cliente_list.jade'
    objects = Cliente.objects.all()
    data = {}
    data['object_list'] = objects
    return render(request, template_name, data)


def cliente_create(request):
    template_name = 'clientes/cliente_form.jade'
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clientes:cliente_list')
    return render(request, template_name, {'form': form, 'status': 'create'})


def cliente_update(request, pk):
    template_name = 'clientes/cliente_form.jade'
    object = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        return redirect('clientes:cliente_list')
    return render(request, template_name, {'form': form, 'fk': pk})


def cliente_delete(request, pk):
    template_name = 'clientes/confirm_delete.jade'
    object = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        object.delete()
        return redirect('clientes:cliente_list')
    return render(request, template_name, {'object': object})


###################
### CRUD CONTATOS
###################
class ContatoForm(forms.BetterModelForm):
    class Meta:
        model = Contato


def contato_list(request, fk):
    template_name = 'clientes/contato_list.jade'
    objects = Contato.objects.filter(cliente__id=fk)
    data = {}
    data['object_list'] = objects
    return render(request, template_name, data)


def contato_create(request):
    template_name = 'clientes/form.jade'
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        contato = form.save()
        return redirect(reverse('clientes:contato_list', args=(contato.cliente.pk,)))
    return render(request, template_name, {'form': form})


def contato_update(request, pk):
    template_name = 'clientes/form.jade'
    object = get_object_or_404(Contato, pk=pk)
    form = ContatoForm(request.POST or None, instance=object)
    if form.is_valid():
        contato = form.save()
        return redirect(reverse('clientes:contato_list', args=(contato.cliente.pk,)))
    return render(request, template_name, {'form': form})


def contato_delete(request, pk):
    template_name = 'clientes/confirm_delete.jade'
    object = get_object_or_404(Contato, pk=pk)
    cliente_id = object.cliente.pk
    if request.method == 'POST':
        object.delete()
        return redirect(reverse('clientes:contato_list', args=(cliente_id,)))
    return render(request, template_name, {'object': object})


###################
### CRUD CONFIGURACAO
###################    
class ConfiguracaoForm(forms.BetterModelForm):
    class Meta:
        model = Configuracao


def configuracao_list(request, fk):
    template_name = 'clientes/configuracao_list.jade'
    objects = Configuracao.objects.filter(cliente__id=fk)
    data = {}
    data['object_list'] = objects
    return render(request, template_name, data)


def configuracao_create(request):
    template_name = 'clientes/form_fileupload.jade'
    if request.method == 'POST':
        form = ConfiguracaoForm(request.POST, request.FILES)
        if form.is_valid():
            configuracao = form.save()

            return redirect(reverse('clientes:configuracao_list', args=(configuracao.cliente.pk,)))
    else:
        form = ConfiguracaoForm()  # A empty, unbound form

    # Render list page with the documents and the form
    return render(request, template_name, {'form': form})


def configuracao_update(request, pk):
    template_name = 'clientes/form_fileupload.jade'
    object = get_object_or_404(Configuracao, pk=pk)
    if request.method == 'POST':
        form = ConfiguracaoForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            configuracao = form.save()

        return redirect(reverse('clientes:configuracao_list', args=(configuracao.cliente.pk,)))
    else:
        form = ConfiguracaoForm(request.POST or None, instance=object)
    return render(request, template_name, {'form': form})


def configuracao_delete(request, pk):
    template_name = 'clientes/confirm_delete.jade'
    object = get_object_or_404(Configuracao, pk=pk)
    cliente_id = object.cliente.pk
    if request.method == 'POST':
        object.delete()
        return redirect(reverse('clientes:configuracao_list', args=(cliente_id,)))
    return render(request, template_name, {'object': object})


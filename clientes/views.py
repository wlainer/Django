# Create your views here.
from django.core.urlresolvers import reverse

from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from form_utils import forms

from clientes.models import UF, Cidade, Cliente, Configuracao, Contato


# ##################
# ## CRUD ESTADO
# ##################
class UFForm(ModelForm):
    class Meta:
        model = UF


def uf_list(request):
    template_name = 'clientes/uf_list.html'
    objects = UF.objects.all()
    data = {}
    data['object_list'] = objects
    return render(request, template_name, data)


def uf_create(request):
    template_name = 'clientes/uf_form.html'
    form = UFForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clientes:uf_list')
    return render(request, template_name, {'form': form})


def uf_update(request, pk):
    template_name = 'clientes/uf_form.html'
    object = get_object_or_404(UF, pk=pk)
    form = UFForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        return redirect('clientes:uf_list')
    return render(request, template_name, {'form': form})


def uf_delete(request, pk):
    template_name = 'clientes/uf_confirm_delete.html'
    object = get_object_or_404(UF, pk=pk)
    if request.method == 'POST':
        object.delete()
        return redirect('clientes:uf_list')
    return render(request, template_name, {'object': object})


###################
### CRUD CIDADE
###################    
class CidadeForm(ModelForm):
    class Meta:
        model = Cidade


def cidade_list(request):
    template_name = 'clientes/cidade_list.html'
    objects = Cidade.objects.all()
    data = {}
    data['object_list'] = objects
    return render(request, template_name, data)


def cidade_create(request):
    template_name = 'clientes/cidade_form.html'
    form = CidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clientes:cidade_list')
    return render(request, template_name, {'form': form})


def cidade_update(request, pk):
    template_name = 'clientes/cidade_form.html'
    object = get_object_or_404(Cidade, pk=pk)
    form = CidadeForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        return redirect('clientes:cidade_list')
    return render(request, template_name, {'form': form})


def cidade_delete(request, pk):
    template_name = 'clientes/cidade_confirm_delete.html'
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
    template_name = 'clientes/cliente_list.html'
    objects = Cliente.objects.all()
    data = {}
    data['object_list'] = objects
    return render(request, template_name, data)


def cliente_create(request):
    template_name = 'clientes/cliente_form.html'
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clientes:cliente_list')
    return render(request, template_name, {'form': form, 'status': 'create'})


def cliente_update(request, pk):
    template_name = 'clientes/cliente_form.html'
    object = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        return redirect('clientes:cliente_list')
    return render(request, template_name, {'form': form, 'fk': pk})


def cliente_delete(request, pk):
    template_name = 'clientes/cliente_confirm_delete.html'
    object = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        object.delete()
        return redirect('clientes:cliente_list')
    return render(request, template_name, {'object': object})


###################
### CRUD CONTATOS
###################
class ContatoForm(ModelForm):
    class Meta:
        model = Contato


def contato_list(request, fk):
    template_name = 'clientes/contato_list.html'
    objects = Contato.objects.filter(cliente__id=fk)
    data = {}
    data['object_list'] = objects
    return render(request, template_name, data)


def contato_create(request):
    template_name = 'clientes/contato_form.html'
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        contato = form.save()
        return redirect(reverse('clientes:contato_list', args=(contato.cliente.pk,)))
    return render(request, template_name, {'form': form})


def contato_update(request, pk):
    template_name = 'clientes/contato_form.html'
    object = get_object_or_404(Contato, pk=pk)
    form = ContatoForm(request.POST or None, instance=object)
    if form.is_valid():
        contato = form.save()
        return redirect(reverse('clientes:contato_list', args=(contato.cliente.pk,)))
    return render(request, template_name, {'form': form})


def contato_delete(request, pk):
    template_name = 'clientes/contato_confirm_delete.html'
    object = get_object_or_404(Contato, pk=pk)
    cliente_id = object.cliente.pk
    if request.method == 'POST':
        object.delete()
        return redirect(reverse('clientes:contato_list', args=(cliente_id,)))
    return render(request, template_name, {'object': object})


###################
### CRUD CONFIGURACAO
###################    
class ConfiguracaoForm(ModelForm):
    class Meta:
        model = Configuracao


def configuracao_list(request, fk):
    template_name = 'clientes/configuracao_list.html'
    objects = Configuracao.objects.filter(cliente__id=fk)
    data = {}
    data['object_list'] = objects
    return render(request, template_name, data)


def configuracao_create(request):
    template_name = 'clientes/configuracao_form.html'
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
    template_name = 'clientes/configuracao_form.html'
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
    template_name = 'clientes/configuracao_confirm_delete.html'
    object = get_object_or_404(Configuracao, pk=pk)
    cliente_id = object.cliente.pk
    if request.method == 'POST':
        object.delete()
        return redirect(reverse('clientes:configuracao_list', args=(cliente_id,)))
    return render(request, template_name, {'object': object})


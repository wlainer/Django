# Create your views here.
from django.core.urlresolvers import reverse

from django.shortcuts import render, redirect, get_object_or_404

from clientes.models import UF, Cidade, Cliente, Configuracao, Contato
from clientes.forms import CidadeForm, ClienteForm, ContatoForm, UFForm, ConfiguracaoForm, PesquisaForm


###################
### CRUD CLIENTE
###################    
def cliente_list(request):
    template_name = 'clientes/cliente_list.jade'
    objects = Cliente.objects.all()
    if request.method == "POST":
        form = PesquisaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            filtro = data['pesquisar']
            objects = Cliente.objects.filter(nome__contains=filtro)
    form = PesquisaForm()
    data = {}
    data['object_list'] = objects
    data['form'] = form
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
def contato_list(request, pk):
    template_name = 'clientes/contato_list.jade'
    objects = Contato.objects.filter(cliente__id=pk)
    data = {}
    data['object_list'] = objects
    data['id'] = pk
    return render(request, template_name, data)


def contato_create(request, pk):
    template_name = 'clientes/form.jade'
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        contato = form.save(commit = False)
        contato.cliente = Cliente.objects.get(pk =pk)
        contato.save()
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
def configuracao_list(request, pk):
    template_name = 'clientes/configuracao_list.jade'
    objects = Configuracao.objects.filter(cliente__id=pk)
    data = {}
    data['object_list'] = objects
    data['id'] = pk
    return render(request, template_name, data)


def configuracao_create(request, pk):
    template_name = 'clientes/form_fileupload.jade'
    if request.method == 'POST':
        form = ConfiguracaoForm(request.POST, request.FILES)
        if form.is_valid():
            configuracao = form.save(commit = False)
            configuracao.cliente = Cliente.objects.get(pk = pk)
            configuracao.save()

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


# ##################
# ## CRUD ESTADO
# ##################
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

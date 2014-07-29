from tastypie.resources import ModelResource
from clientes.models import Cliente

class ClienteResource(ModelResource):
    class Meta: queryset = Cliente.objects.all()
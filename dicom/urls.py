from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from clientes.api import ClienteResource

cliente_resource = ClienteResource()


urlpatterns = patterns('',
    #rest service cliente
    url(r'^api/', include(cliente_resource.urls)),

    #static
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT}),
    #media
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    #index
    url(r'^$', 'dicom.views.home', name="home"),

)
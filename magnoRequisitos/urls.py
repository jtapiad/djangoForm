"""magnoRequisitos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from solicitudes import views

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', Registrar.as_view(),name="registrar"),
#     url(r'^(?P<id>\d+)$', EditarRegistro.as_view(),name="editar"),
#     url(r'^listado', ListadoRegistros.as_view(),name="listar"),
#     url(r'^(?P<id>\d+)/borrar$', eliminar.as_view(),name="BorrarRegistro"),
# ]

#url class based view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.RegistroList.as_view(), name="registro_list"),
    url(r'^crear$', views.RegistroCrear.as_view(), name="registro_crear"),
    url(r'^edit/(?P<pk>\d+)$', views.RegistroUpdate.as_view(), name="registro_edit"),
    url(r'^delete/(?P<pk>\d+)$', views.eliminarRegistro, name="registro_delete"),
]

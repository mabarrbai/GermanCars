from django.conf.urls import include, url
from penhas import views

urlpatterns = [
	url(r'^$', fecha_actual),
    url(r'^partido/equipos/$', views.formar_equipos),
    url(r'^penhas/$', views.lista_penha),
    url(r'^penhas/(?P<pk>[0-9]+)/$', views.penha_detail),
]

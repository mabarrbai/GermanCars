from django.conf.urls import patterns, url
from partidos_penha import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^reclama_datos/$', views.reclama_datos, name='reclama_datos'),
        url(r'^megusta_jugador/$', views.megusta_jugador, name='megusta_jugador'),
        url(r'^(?P<penha_name>[\w\-]+)/$', views.penha, name='penha'),
        url(r'^(?P<penha_name>[\w\-]+)/add_jugador/$', views.add_jugador, name='add_jugador'),               
        )

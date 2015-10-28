from django.conf.urls import include, url
from penhas.views import formar_equipos

urlpatterns = [
    url(r'^partido/equipos/$', formar_equipos),
]

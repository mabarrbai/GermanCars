from django.conf.urls import include, url
from penhas import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'jugadores', views.JugadorViewSet)
router.register(r'penhas', views.PenhaViewSet)

urlpatterns = [
    url(r'^partido/equipos/$', views.formar_equipos),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

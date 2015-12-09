# TusPachangas
[![Build Status](https://travis-ci.org/mabarrbai/TusPachangas.svg?branch=master)](https://travis-ci.org/mabarrbai/TusPachangas)
[![Build Status](https://snap-ci.com/mabarrbai/TusPachangas/branch/master/build_image)](https://snap-ci.com/mabarrbai/TusPachangas/branch/master)
[![Deploy to Heroku TusPachangas](http://blog.openplans.org/wp-content/uploads/2014/12/Screen-Shot-2014-12-03-at-10.47.32-PM.png)](https://tuspachangas.herokuapp.com/)

Proyecto de la asignatura Infraestructura Virtual en conjunto con la de Desarrollo de Aplicaciones para Internet

##Introducción
La aplicación web que voy a realizar será la de una aplicación que se encargue de gestionar peñas de fútbol de amigos(aunque podría ser ampliada a otros deportes). Entre las funcionalidades que tendrá serán principalmente:
* Registrar peñas.
* Añadir los componentes de la peña.
* Clasificaciones de los componentes, según partidos ganados, goles, etc.
* Formación aleatoria de equipos.
* Avisos particulares a componentes.
* Gestión de campeonatos y disputa de partidos entre peñas.

[**Más información**](https://github.com/mabarrbai/TusPachangas/blob/master/doc/intro.md)


##Sistemas de tests e Integración continua
Para el sistema de test, he usado un sistema de testeos unitarios específicos de Django,la subclase **[django.test.TestCase](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TestCase)**, el cual se basa en la biblioteca de testeos unitarios de Python, **[unittest](https://docs.python.org/3/library/unittest.html#module-unittest)** y más específicamente en la subclase **[unittest.TestCase](https://docs.python.org/3/library/unittest.html#unittest.TestCase)**. 
He usado este sistema de testeo ya que está enfocado directamente a proyectos con Django y a sus funcionalidades como vistas,modelos,etc.

Para la integración continua, he usado el sistema de **Travis CI** ya que lo indiqué en la planificación inicial y además he comprobado su facilidad de uso y su gran utilidad. Ante cualquier *push* al repositorio de mi proyecto (el cual está sincronizado con Travis), Travis se encarga de llevar a cabo las pruebas de integración continua indicadas en el fichero *.travis.yml*.
[**Más información**](https://github.com/mabarrbai/TusPachangas/blob/master/doc/CI.md)

#Despliegue de la aplicación en un PaaS
En esta parte, el objetivo principal ha sido desplegar nuestra aplicación sobre un PaaS. 
En mi caso, me he decidido por Heroku, ya que durante su utilización en los ejercicios me ha parecido simple de comprender y usar porque funciona con una simple configuración, además de ser gratuito por lo que cubre todos mis objetivos. Tambien admite múltiples lenguajes de programación, entre ellos Python con el framework Django sobre el cual está construida mi aplicación web.

[**Más información**](https://github.com/mabarrbai/TusPachangas/blob/master/doc/PAAS.md)


#Entorno de pruebas
Para el entorno de pruebas se ha utilizado Docker el cual está basado en un sistema de contenedores. Concretamente, he creado una imagen basada en Ubuntu la cual tiene la aplicación TusPachangas descargada y preparada para su ejecución y la cual puede ser obtenida con una sola orden desde DockerHub.

[**Más información**](https://github.com/mabarrbai/TusPachangas/blob/master/doc/docker.md)





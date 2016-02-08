# TusPachangas
[![Build Status](https://travis-ci.org/mabarrbai/TusPachangas.svg?branch=master)](https://travis-ci.org/mabarrbai/TusPachangas)

[![Deploy to Heroku TusPachangas](http://blog.openplans.org/wp-content/uploads/2014/12/Screen-Shot-2014-12-03-at-10.47.32-PM.png)](https://tuspachangas.herokuapp.com/partidos/penha)
[![Deploy Azure](https://camo.githubusercontent.com/9285dd3998997a0835869065bb15e5d500475034/687474703a2f2f617a7572656465706c6f792e6e65742f6465706c6f79627574746f6e2e706e67)](http://tuspachangas.cloudapp.net/partidos/penha/)

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

##Despliegue de la aplicación en un PaaS
En esta parte, el objetivo principal ha sido desplegar nuestra aplicación sobre un PaaS. 
En mi caso, me he decidido por Heroku, ya que durante su utilización en los ejercicios me ha parecido simple de comprender y usar porque funciona con una simple configuración, además de ser gratuito por lo que cubre todos mis objetivos. Tambien admite múltiples lenguajes de programación, entre ellos Python con el framework Django sobre el cual está construida mi aplicación web.

[**Más información**](https://github.com/mabarrbai/TusPachangas/blob/master/doc/PAAS.md)


##Entorno de pruebas
Para el entorno de pruebas se ha utilizado Docker el cual está basado en un sistema de contenedores. Concretamente, he creado una imagen basada en Ubuntu la cual tiene la aplicación TusPachangas descargada y preparada para su ejecución y la cual puede ser obtenida con una sola orden desde DockerHub. [Imagen en DockerHub](https://hub.docker.com/r/mabarrbai/tuspachangas/)

[**Más información**](https://github.com/mabarrbai/TusPachangas/blob/master/doc/docker.md)


##Despliegue de la aplicación en un IaaS
También está disponible la posibilidad de desplegar la aplicación en un IaaS.
Esto se puede llevar a cabo con el script que se aporta en la carpeta **scripts** de nombre **deployAzure.sh**. Este script se encarga de instalar todas las herramientas necesarias para el despliegue y de lanzar Vagrant configurado para crear y configurar una máquina virtual en Microsoft Azure y para utilizar Ansible como provisionador.
Para que la ejecución del script se haga de forma correcta, es **necesario tener previamente una cuenta en Azure además de configurada correctamente. Los detalles de dicha configuración se pueden leer en el siguiente enlace.**
[**Más información**](https://github.com/mabarrbai/TusPachangas/blob/master/doc/IaaS.md)





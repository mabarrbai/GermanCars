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
	
##Infraestructura
Como infraestructura necesaria para la aplicación será necesario:
* **Servidores web** configurados correctamente, entre los que habrá varios de producción, uno de desarrollo, y otro que actuará como balanceador de carga e implementará funcionalidades de seguridad como puede ser un firewall. También sería posibley puede que conveniente, la separación firewall/balanceador. De esta forma, se tendría el firewall como rimera puerta de entrada, y si es admitida la petición,entraría el balanceador de carga a actuar.

* **Servidores de bases de datos** para almacenar todo el contenido de la aplicación web. Tener en cuenta que las bases de datos estarán replicadas continuamente.
	
* **Servidor de correo**, para el envío de notificaciones a peñas y componentes.	
	
##Herramientas
La aplicación será desarrollada con un framework web como **Django**.
Para ir siguiendo el desarrollo de la aplicación web y testeándola, se usará **Travis CI**, con el que se podrá, por ejemplo, probar la aplicación contra distintas configuraciones.

##Comentarios
*Según avance la asignatura, se irán refinando (añadiendo, eliminando, modificando) la funcionalidad, infraestructura y herramientas a utilizar.*
	
##Inscripción en el [certamen de proyectos de la UGR](http://osl.ugr.es/bases-de-los-premios-a-proyectos-libres-de-la-ugr/)
![Inscripción al certamen de la UGR](http://i1016.photobucket.com/albums/af281/raperaco/inscripcionCertamenUGR_zps34rx09mo.png)

#Segundo hito del proyecto
En este segundo hito, ya he comenzado mi proyecto de aplicación web con el framework **Django**. Ahora mismo sólo hay desarollada una vista, que mezcla los jugadores de una peña y los divide en dos equipos para disputar el partido semanal. También dispongo de una parte del modelo de la aplicación, utilizando el sistema **SQLite**.

##Herramienta de construcción
Como herramienta de construcción he usado **make** mediante un fichero Makefile. Me he decidido a usar esta porque cumple su función correctamente y es con la que más he trabajado.
He creado una serie de objetivos en el Makefile:
* doc (genera la documentación)
* install (instala los paquetes requeridos para la aplicación)
* test (testea el modelo de la aplicación (bases de datos))
* start (arranca el servidor web de la app)

##Sistemas de tests e Integración continua
Para el sistema de test, he usado un sistema de testeos unitarios específicos de Django,la subclase **[django.test.TestCase](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TestCase)**, el cual se basa en la biblioteca de testeos unitarios de Python, **[unittest](https://docs.python.org/3/library/unittest.html#module-unittest)** y más específicamente en la subclase **[unittest.TestCase](https://docs.python.org/3/library/unittest.html#unittest.TestCase)**. 
He usado este sistema de testeo ya que está enfocado directamente a proyectos con Django y a sus funcionalidades como vistas,modelos,etc.

Para la integración continua, he usado el sistema de **Travis CI** ya que lo indiqué en la planificación inicial y además he comprobado su facilidad de uso y su gran utilidad. Ante cualquier *push* al repositorio de mi proyecto (el cual está sincronizado con Travis), Travis se encarga de llevar a cabo las pruebas de integración continua indicadas en el fichero *.travis.yml*.
En este fichero he indicado las instrucciones para instalar y testear la aplicación web. Para ello he utilizado las órdenes a través de la herramienta de construcción make con el fichero Makefiile, ya explicado en el paso anterior.
De esta manera, estamos haciendo una comprobación doble. Por una parte se prueba que el fichero Makefile que tenga el formato correcto y realice las operaciones adecuadas, y por otra parte se prueba la instalación y testeo de la aplicación web.
Se puede ver el resultado de las pruebas superadas de integración continua con Travis en las siguientes imágenes:
* Enlace directo al testeo en Travis:[![Build Status](https://travis-ci.org/mabarrbai/TusPachangas.svg?branch=master)](https://travis-ci.org/mabarrbai/TusPachangas)
* Capturas tomadas desde Travis:
![TravisMake1](http://i1016.photobucket.com/albums/af281/raperaco/travisMake1_zpswr5eafgc.png)
![TravisMake2](http://i1016.photobucket.com/albums/af281/raperaco/travisMake1_zps2wkpmeas.png)
![TravisMake3](http://i1016.photobucket.com/albums/af281/raperaco/travisMake2_zpsfmoiny2p.png)

#Despliegue de la aplicación en un PaaS
En esta parte, el objetivo principal ha sido desplegar nuestra aplicación sobre un PaaS. 
En mi caso, me he decidido por Heroku, ya que durante su utilización en los ejercicios me ha parecido simple de comprender y usar porque funciona con una simple configuración, además de ser gratuito por lo que cubre todos mis objetivos. Tambien admite múltiples lenguajes de programación, entre ellos Python con el framework Django sobre el cual está construida mi aplicación web.
Los pasos llevados a cabo para desplegar mi aplicación en Heroku han sido los siguientes:
* Registrarme en Heroku, obviamente.
* Descargar el toolbelt de Heroku, el cual nos proporciona una serie de herramientas necesarias para poder trabajar con Heroku.
~~~
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
~~~
* Nos logueamos en Heroku desde el terminal.
~~~ 
heroku login
~~~
* Crear un fichero **Procfile** en la carpeta raíz de nuestro proyecto, en el que indicamos los pasos necesarios para desplegar la aplicación web en Heroku. En nuestro caso:
~~~
web: gunicorn TusPachangas.wsgi --log-file -
~~~
* Actualizar el fichero de dependencias **requirements.txt**. Tras actualizarlo, borrar la entrada correspondiente a nuestra aplicación ya que no es una dependencia, sino el objetivo a conseguir. En mi caso, TusPachangas.
~~~
pip freeze > requirements.txt
~~~
* Modificar el fichero **settings.py** para indicar que cuando la aplicación se encuentre en Heroku, use la base de datos que provee Heroku. Para ello, hay que obtener la URL de la base de datos de Heroku la cual se puede obtener desde el panel de control de Heroku. El código a añadir al fichero será el siguiente:
~~~
import dj_database_url
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
ON_HEROKU = os.environ.get('PORT')
if ON_HEROKU:
    DATABASE_URL='postgres://fhtyiztxysbrdn:WI7TLSaRrLYxotdwfryDYIQwn2@ec2-54-225-192-128.compute-1.amazonaws.com:5432/demv8ll9orcqeg'
    DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
~~~
* En el fichero wsgi.py, añadir el siguiente código:
~~~
from django.core.wsgi import get_wsgi_application
from dj_static import Cling
application = Cling(get_wsgi_application())
~~~
* Preparar todos los ficheros modificados para subirlos a un repositorio GitHub.
~~~
git init
git add .
git commit -m "my django app"
~~~
* Crear un nuevo repositorio remoto git para subir la aplicación a Heroku.
~~~
heroku create
~~~
* Subir la aplicación al nuevo repositorio creado.
~~~
git push heroku master
~~~
* Aplicar los cambios sobre la base de datos de Heroku y crear el superusuario de nuestra aplicación.
~~~
heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
~~~
* Ya se puede abrir la aplicación desplegada.
~~~
heroku open
~~~
* Vemos que el comando anterior nos abre una ventana de navegador con nuestra aplicación desplegada (si es que todo ha salido bien) pero con una URL un tanto rara. Si se quiere cambiar, se puede hacer desde el panel de control de Heroku, en la pestaña Ajustes. Una vez cambiado, hay que actualizar el nombre del repositorio remoto de nuestra aplicación con el nuevo nombre, para ello hay que ejecutar(en mi caso):
~~~
git remote rm heroku
heroku git:remote -a tuspachangas
~~~

Habiendo realizado estos pasos citados sin errores, la aplicación ya estará desplegada en Heroku, usando la base de datos PostgreSQL que Heroku proporciona.Ya solo queda rellenar la base de datos, lo cual puede realizarlo el superusuario de la aplicación  creado anteriormente en la ruta **/admin/**.
Por tanto, mi aplicación desplegada en el servicio gratuito de Heroku tendrá la URL **https://tuspachangas.herokuapp.com/** y queda de la siguiente forma:
* La ruta **/**
![heroku](http://i1016.photobucket.com/albums/af281/raperaco/heroku_zpsgojniwgh.png)
* La ruta **/penhas/**
![heroku1](http://i1016.photobucket.com/albums/af281/raperaco/heroku1_zpswwx1rjgb.png)
* Las rutas en las que se muestra en detalle cada peña individualmente. Se accede a traves del identificador pk, el cual se puede ver que se obtiene en la ruta /penhas/ en la anterior imagen. Por ejemplo para la peña con identificador 2, la ruta será **/penhas/2/**
![heroku2](http://i1016.photobucket.com/albums/af281/raperaco/heroku2_zpsyw5ew7gr.png)

Además de todo lo anterior, que sería lo básico para desplegar la aplicación en Heroku, he conectado GitHub con Heroku para realizar un despliegue automático cada vez que se suban nuevos fuentes al repositorio GitHub de la aplicación habiendo superado previamente los tests. De esta forma, cada vez que modifique un fichero fuente y lo suba al repositorio con la orden **git push**, automáticamente la aplicación será testeada con los nuevos cambios en Travis y SnapCI y si los tests se superan, la aplicación será desplegada con los nuevos cambios en Heroku.

Hay un enlace a mi aplicación desplegada en Heroku a través de la URL antes citada, o a través del badge que hay al inicio de este documento.

##Avance de la aplicación
Se han realizado dos vistas generales más, las correspondientes a **/penhas/** y la correspondiente **/penhas/x/**. En ellas se serializa el acceso a base de datos y se muestran los valores obtenidos en formato **JSON**. En la portada, se han puesto enlaces a estas rutas.
Para las nuevas rutas, se han creado tests específicos (en el fichero tests.py) en los cuales se comprueba que se reciba la ruta correctamente, es decir que el código HTTP sea el 200 y que el contenido recibido es del tipo JSON.


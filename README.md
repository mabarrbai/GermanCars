# TusPachangas
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

##Integración continua
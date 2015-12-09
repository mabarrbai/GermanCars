FROM ubuntu:latest

#Autor
MAINTAINER Manuel Alejandro Barranco Bailon <mabarranco@correo.ugr.es>

#Actualizar Sistema Base
RUN sudo apt-get -y update

# Instalar Python
RUN sudo apt-get -y install python-setuptools
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo easy_install pip

#Descargar aplicacion
RUN sudo apt-get -y install git
RUN sudo git clone https://github.com/mabarrbai/TusPachangas.git

#Instalar aplicacion
RUN cd TusPachangas/ && pip install -r requirements.txt
RUN cd TusPachangas/ && python manage.py syncdb --noinput

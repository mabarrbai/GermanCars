#!/bin/bash

#Descarga docker
sudo apt-get install -y docker.io
# Inicia el servicio docker
sudo service docker start
#Descarga la imagen
sudo docker pull mabarrbai/tuspachangas
#Ejecuta la imagen
sudo docker run -i -t mabarrbai/tuspachangas /bin/bash 

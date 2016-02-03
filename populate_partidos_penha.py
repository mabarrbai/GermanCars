import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TusPachangas.settings')

import django
django.setup()

from partidos_penha.models import Penha, Jugador


def populate():
    penha_quintos = add_penha('Los Quintos', 'Maracena', 'Av. Jose Comino, Maracena, Granada, Spain')

    add_jugador(penha=penha_quintos,
        nombre="Gabriel",
        apellidos="Garcia")

    add_jugador(penha=penha_quintos,
        nombre="Vicente",
        apellidos="Gimenez Casas")

    add_jugador(penha=penha_quintos,
        nombre="Pedro",
        apellidos="Morcillo")

    penha_pelicanos = add_penha('Los Pelicanos', 'Granada', 'Paseo Prof. Juan Ossorio, Granada, Spain')

    add_jugador(penha=penha_pelicanos,
        nombre="Pedro",
        apellidos="Lopez Ruiz")

    add_jugador(penha=penha_pelicanos,
        nombre="Quique",
        apellidos="Vela")

    add_jugador(penha=penha_pelicanos,
        nombre="Xisco",
        apellidos="Neruda")

    penha_jamon = add_penha('El Jamon', 'Granada', 'Maria Goyri 36, La Chana, Granada, Spain')

    add_jugador(penha=penha_jamon,
        nombre="Nino",
        apellidos="Ruiz")

    add_jugador(penha=penha_jamon,
        nombre="Carlos",
        apellidos="Vela")

    add_jugador(penha=penha_jamon,
        nombre="Mateo",
        apellidos="Lopez")

    penha_historica = add_penha('Historica', 'Armilla', 'Leon 0, Armilla, Granada, Spain')

    add_jugador(penha=penha_historica,
        nombre="Luis",
        apellidos="Pardo")

    add_jugador(penha=penha_historica,
        nombre="Sergio",
        apellidos="Garcia")

    add_jugador(penha=penha_historica,
        nombre="Andres",
        apellidos="Liso")

    penha_fuente = add_penha('La Fuente', 'Fuente Vaqueros', 'Av Andalucia 195, Fuente Vaqueros, Granada, Spain')

    add_jugador(penha=penha_fuente,
        nombre="Salva",
        apellidos="Rueda")

    add_jugador(penha=penha_fuente,
        nombre="Alex",
        apellidos="Casado")

    add_jugador(penha=penha_fuente,
        nombre="Pinos",
        apellidos="Peligroso")

    # Print out what we have added to the user.
    for p in Penha.objects.all():
        for j in Jugador.objects.filter(penha=p):
            print "- {0} - {1}".format(str(p), str(j))

def add_jugador(penha, nombre, apellidos):
    j = Jugador.objects.get_or_create(penha=penha, nombre=nombre)[0]
    j.apellidos=apellidos
    j.save()
    return j

def add_penha(name,city,address):
    p = Penha.objects.get_or_create(nombre=name, ciudad=city, direccion=address)[0]
    return p

# Start execution here!
if __name__ == '__main__':
    print "Starting partidos_penha population script..."
    populate()
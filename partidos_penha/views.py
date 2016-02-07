from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from partidos_penha.models import Penha
from partidos_penha.models import Jugador
from partidos_penha.forms import JugadorForm

from django.http import JsonResponse

from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import PenhaSerializer

def index(request):
	penha_list = Penha.objects.order_by('nombre')[:10]
	jugador_list = Jugador.objects.order_by('-megusta')[:10]
	context_dict = {'penhas': penha_list, 'jugadores': jugador_list}
	return render(request, 'partidos_penha/index.html', context_dict)

def about(request):
	context_dict = {'boldmessage': "Esta es la pagina /about/"}
	return render(request, 'partidos_penha/about.html', context_dict)		
    
def penha(request, penha_name):

    context_dict = {}

    try:
        penha = Penha.objects.get(slug=penha_name)
        context_dict['penha_name'] = penha.nombre

        jugadores = Jugador.objects.filter(penha=penha)

        context_dict['jugadores'] = jugadores
        
        context_dict['penha'] = penha

        #actualizar el contador de visitas
        penha.visitas = penha.visitas + 1
        penha.save()
    except Penha.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'partidos_penha/penha.html', context_dict)

def add_jugador(request, penha_name):
    try:
        penha = Penha.objects.get(slug=penha_name)
    except Penha.DoesNotExist:
        penha = None

    if request.method == 'POST':        

        if penha != None:    
            form = JugadorForm(request.POST)

            if form.is_valid():
                #obtengo los valores del formulario del nuevo jugador pero no los envio para anhadir la penha obtenida de la URL
                jugador = form.save(commit=False)

                jugador.penha = penha

                jugador.save()
                return HttpResponseRedirect('/partidos/penha/%s/' % penha.slug)
            else:
                print form.errors
        else:
            print 'La penha '+penha_name+' no existe. No se puede insertar un jugador en una penha inexistente.'
    else:    
        form = JugadorForm()

    return render(request, 'partidos_penha/add_jugador.html', {'form': form, 'penha': penha})

def reclama_datos(request):
    lista_penhas = Penha.objects.order_by('-visitas')[0:5]
     
    datos = {}

    datos['penhas'] = [lista_penhas[0].nombre,lista_penhas[1].nombre,lista_penhas[2].nombre,lista_penhas[3].nombre,lista_penhas[4].nombre]

    datos['visitas'] = [lista_penhas[0].visitas,lista_penhas[1].visitas,lista_penhas[2].visitas,lista_penhas[3].visitas,lista_penhas[4].visitas]
   
    return JsonResponse(datos,safe=False)

def megusta_jugador(request):
    datos = {}

    jug_id = None
    if request.method == 'GET':
    	jug_id = request.GET['jugador_id']
    	
    megusta = 0
    if jug_id:
    	jug = Jugador.objects.get(id=int(jug_id))
    	if jug:
    		megusta = jug.megusta + 1
    		jug.megusta = megusta
    		jug.save()
	
	return HttpResponse(megusta)
	
class JSONResponse(HttpResponse):
    """
    Una respuesta HTTP que renderiza el contenido en JSON
    """
    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def lista_penha(request):
    """
    Lista el codigo de todas las penhas, o crea una nueva
    """
    if request.method == 'GET':
        penhas = Penha.objects.all()
        serializer = PenhaSerializer(penhas, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PenhaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def penha_detail(request, pk):
    """
    Recupera,actualiza o borra el codigo de una penha
    """
    try:
        penha = Penha.objects.get(pk=pk)
    except Penha.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PenhaSerializer(penha)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PenhaSerializer(penha, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        penha.delete()
        return HttpResponse(status=204)
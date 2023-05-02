
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader 

def saludo(request):   #Nuestra primera vista :) 
	return HttpResponse("Hola Django - Coder, esta es mi primera VISTA, acá puedo escribir lo que quiera Lucas")

def vista_dos(request):
    return HttpResponse("<br><br> estoy en la segunda VISTA, aún no entiendo todo...:) ")

def primer_template(self):
    nomb='Lucas'
    ap='Olhasso'
    diccionario={'nombre':nomb, 'apellido':ap}
    #miHtml = open("C:/Users/Lucas/repo_lucas_coder/Tercera_preentrega_Olhasso/proyectoolhasso/proyectoolhasso/plantillas/template1.html")
    #plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context
    #miHtml.close() #Cerramos el archivo
    #miContexto = Context(diccionario) #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo
    #documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento
    plantilla= loader.get_template('template1.html')
    documento = plantilla.render(diccionario) #Aca renderizamos la plantilla en documento
    return HttpResponse(documento)

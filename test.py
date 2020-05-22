from cmd import GenerarClase

dic={'NombreC':'Collector_app',
     'atributo':['id'],
     'tipo':['numero']}

a=GenerarClase()
estado=False

#estado=a.CrearArchivo(dic)
#estado=a.LimpiarArchivo(nombre)
estado=a.Principal(dic)
#respuesta=a.CrearSet(dic)
#print(respuesta)
#lista=a.CrearSTR(dic)
#print(lista)
print(estado)
from Final import diccionario
from cmd import GenerarClase
import time
def Iterador(diccionario):
    #diccionario base para utilizar el generador
    dic={'NombreC':'', 'atributo':[],'tipo':[]}

    #print(diccionario)
    numero=1
    try:
        print("PASO "+str(numero)+": Cantidad de Clases :"+str(len(diccionario['nombres'])))
        numero+=1
        #time.sleep(0.3)
        for indiceClase in range(0,len(diccionario)):
            atributo=[]

            
            nombres=""
            # obtengo el nombre de la clase para un uso posterior
            nombreClase=diccionario['nombres'][indiceClase]
            #Imprimo la clase
            ##print("PASO "+str(numero)+": Nombre de la Clase :"+nombreClase)

            ##genero una variable donde guardo mi nombre  y cambio el valor del diccionario
            nombres=nombreClase
            dic['NombreC']=nombres
            ##print(dic)
            #time.sleep(0.3)
            #devuelvo el nombre de la clase de la persona
            #print(len(diccionario['atributos']))#+" Indice :"+str(indiceClase))

            tipo=[]
            for indiceAtri in range(0,len(diccionario['atributos'])):
                #Obtengo El nombre de la clase del Atributo, en este caso es (persona,mujer,animal)
                nombreAtrib=str(diccionario['atributos'][indiceAtri][1])
                #print(str(indiceAtri))
                #nombre:0 ,casado:1 ,edad:2 altura:3 , raza:4 , sexo:5 , vacuna:6
                #Comparado el nombre del abributo
                if nombreAtrib.__eq__(diccionario['nombres'][indiceClase]):
                    #print("Nombre de la clase: "+nombreClase+" Atributo:"+diccionario['atributos'][indiceAtri][0])
                    #indice es el numero que va de 0 a 6 la longitud de los tipo
                        #  0     1        2     3     4      5       6
                        #texto,boolean,numero,float,float,boolean,boolean
                    for indiceTipo in range(0,len(diccionario['tipos'])):
                        nombreTipo=str(diccionario['tipos'][indiceTipo][2])
                        if nombreTipo.__eq__(diccionario['atributos'][indiceAtri][0]):
                            nombreTipo=str(diccionario['tipos'][indiceTipo][0])
                            ##print("Nombre de la clase: "+nombreClase+" Atributo:"+diccionario['atributos'][indiceAtri][0]+"  tipo de dato:"+nombreTipo)
                            
                            atributo.append(diccionario['atributos'][indiceAtri][0])
                            tipo.append(nombreTipo)
                            ##print("Atributos a guardar hasta el momento :"+str(atributo))
                            dic['atributo']=atributo
                            dic['tipo']=tipo
                            #time.sleep(0.3) 
            print("Diccionario a usar :"+str(dic))
            ejecutar=GenerarClase()
            ejecutar.Principal(dic)
            time.sleep(0.4)

            #dicFinal.append(dic)
            #print(str(dicFinal))
            ##ejecuto el generador de clases en otro lado, ya quedo la aqui
        #print(str(dicFinal))

        
    except Exception as e:
        print("Error :"+str(e))

Iterador(diccionario)

